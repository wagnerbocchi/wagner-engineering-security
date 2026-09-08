# Orchestration / SOAR engine

## Modelo de execução
Cada step deve ter: input schema, output schema, timeout, retry policy, idempotency key, secrets scope,
logs/traces, status e classificação de side effect.

## Estados típicos
pending → running → succeeded | failed | outcome_unknown

Estados auxiliares: waiting_approval, retry_scheduled, cancelled, reconciling, compensation_failed.
Cancelamento local não prova interrupção de uma chamada já enviada ao provider.

## Ações críticas
Suporte human approval, least privilege, dry-run quando possível, audit trail e compensation.

## Connectors
SDK de connector deve padronizar auth, pagination, rate limits, retries, errors, schemas e secret handling.
Versione connector e contract de action.

## Janela de crash e resultado desconhecido

Persistir intenção antes de chamar o provider não torna a operação distribuída atômica. Se o worker
morrer depois do efeito e antes de persistir o resultado, a reentrega deve reconciliar a execução.

```text
operation_key = tenant autenticado + run_id + step_id + action_version
pending -> claim/lease com exclusão atômica -> running -> provider
provider confirmado + resultado persistido -> succeeded -> ack
timeout/crash com efeito incerto -> outcome_unknown -> reconciling
```

Use chave estável do provider quando suportada e registre request ID. Evite dois workers concorrentes
para a mesma operação; lease expirada não garante que o primeiro worker parou. Fencing/condições de
escrita precisam ser compatíveis com o executor e provider.

Consultar apenas “IP já bloqueado” pode refletir outra operação. Correlacione autoria/ID e parâmetros;
se o provider não oferece consulta ou garantia suficiente, mantenha revisão operacional sem retry cego.
Uma chamada HTTP 2xx pode ser somente aceitação: observe a conclusão assíncrona conforme contrato.

## Persistência e autorização

Para estado local + publicação, use outbox transacional quando necessário. Consumers deduplicam
atomicamente com seus efeitos locais; isso não cria exactly-once para API externa. Revalide tenant,
ação, destino e credenciais antes da execução conforme política do produto, inclusive em redelivery.

Compensação tem escopo e autorização próprios. Não remova um bloqueio compartilhado criado por outra
operação ao desfazer uma execução; registre falha de compensação como estado observável.
