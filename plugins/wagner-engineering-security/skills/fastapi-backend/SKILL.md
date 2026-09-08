---
name: fastapi-backend
description: >
  Use quando a tarefa principal for implementar ou corrigir serviço FastAPI/ASGI, contratos Pydantic, persistência, autorização, webhooks ou jobs. Para testes ofensivos da API use api-security-testing; para Python genérico use python-scripting.
---

# FastAPI Backend

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

## Entradas úteis
- versão de Python/FastAPI/Pydantic;
- banco/ORM e estratégia de migração;
- tipo de autenticação e modelo de autorização;
- SLO de latência/throughput;
- natureza dos jobs assíncronos e garantias necessárias.

## Workflow
1. Modele contratos de API e erros antes da implementação.
2. Separe camada HTTP, domínio e infraestrutura quando o domínio justificar.
3. Defina transações, idempotência e concorrência.
4. Escolha sync/async pela natureza das dependências, não por moda.
5. Escolha execução de background por requisitos de durabilidade/retry/escala.
6. Adicione testes, health/readiness e telemetria.

## Background jobs: decisão correta
- `BackgroundTasks`: trabalho curto, best-effort, aceitável perder se o processo morrer.
- fila/worker persistente: quando precisa retry, durabilidade, escalabilidade independente, scheduling ou isolamento.
- CPU-bound: processo/worker separado; não bloquear event loop.
- Não escolher broker/worker apenas pela duração em segundos.

## Segurança
- autorização por recurso/tenant;
- validação estrita de payload;
- rate limit conforme risco;
- secrets fora do código;
- evitar SSRF em URLs controladas pelo usuário;
- limites de upload/body e timeouts.

## Consistência em APIs e jobs
- Derive identidade/tenant de contexto autenticado e vincule-os à consulta, cache e job; campo tenant_id enviado pelo cliente não estabelece autoridade.
- Propague deadline/cancelamento e use clients/pools com ciclo de vida explícito. Código blocking em função async continua bloqueando o event loop.
- Se escrita no banco precisa gerar mensagem, avalie outbox na mesma transação; publicar apenas depois do commit ainda deixa uma janela de perda.
- Para POST repetível, use chave por tenant/operação e fingerprint do payload com unicidade atômica. Mesma chave e payload retorna resultado estável; payload diferente exige conflito definido.
- Teste redelivery concorrente, crash após commit e autorização revogada antes da execução/entrega, conforme a política do produto.

## Recursos

- Para estrutura, lifespan e readiness: [architecture](references/architecture.md).
- Para atomicidade, durabilidade e execução de workers: [jobs](references/jobs.md).
