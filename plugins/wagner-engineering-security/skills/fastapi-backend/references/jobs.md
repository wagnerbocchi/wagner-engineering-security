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
