# Jobs e workers

## Requisitos a perguntar
- Pode perder o job?
- Precisa retry? Quantas vezes?
- É idempotente?
- Precisa agendamento?
- Precisa prioridade/tenant isolation?
- Qual volume e duração?
- Como observar backlog e DLQ?

Celery, Dramatiq, RQ, Temporal e brokers diferentes atendem garantias diferentes. Não presuma uma combinação
como default universal. Para workflows longos e stateful, considere engine de workflow; para jobs simples,
uma fila menor pode ser suficiente.

## Escrita e publicação consistentes

Se o request cria um caso e precisa disparar trabalho, persista caso, registro de idempotência e outbox
na mesma transação. Um dispatcher publica entradas commitadas. Crash após publish e antes do ack pode
repetir a mensagem: consumidor usa inbox/unicidade atômica com seus efeitos locais.

```text
UNIQUE(tenant_id, operation, idempotency_key)
registro = request_fingerprint + resource_id + status/response
mesma chave + mesmo payload -> resultado estável
mesma chave + payload diferente -> conflito conforme contrato
```

Defina retenção da chave e resposta enquanto uma operação está em andamento. GET seguido de INSERT
sem constraint/controle transacional não protege contra requests concorrentes.

Teste rollback antes do commit, crash após commit, reentrega após publish e POSTs concorrentes.
Para efeitos remotos de resultado desconhecido, reconcilie com o provider; outbox não resolve sozinha
a duplicação de uma ação externa. Preserve identidade/tenant e política de autorização até a entrega.
