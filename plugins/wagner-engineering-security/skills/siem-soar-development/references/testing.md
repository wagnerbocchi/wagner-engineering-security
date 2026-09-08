# Testes e observabilidade do produto

## Testes
- parser fixtures e fuzzing de input;
- schema compatibility;
- replay determinístico de eventos;
- detection regression;
- orchestration idempotency/retry;
- tenant-isolation tests;
- load/soak para ingest/search;
- chaos em queue/storage/dependências.

## Métricas
EPS ingestado/aceito/rejeitado, lag, parse failures, normalize latency, detection latency, query p95/p99,
alert volume, queue depth, playbook success/retry/failure, connector rate-limit, cost por tenant.

Trace um event_id/correlation_id ponta a ponta para diagnóstico.

## Casos de aceitação prioritários

| Injeção/cenário | Invariante |
|---|---|
| Credencial A + tenant B no envelope | Rejeição/quarentena; nenhuma consulta/ação com credencial de B |
| Redelivery concorrente | Unicidade atômica local e reconciliação de efeito externo |
| Crash após provider e antes do commit | Resultado desconhecido, sem repetição cega |
| Evento atrasado e fora de ordem | Resultado conforme política temporal declarada |
| Busca/cache/export com IDs de outro tenant | Nenhum conteúdo ou efeito cruzado |
| Parser novo em replay | Versão escolhida e mudança de semântica rastreáveis |
| Timeout/429/DLQ por tenant ruidoso | Outros tenants dentro das quotas/SLOs acordados |

Use fixtures sintéticas e falhas injetadas em fakes/ambiente de teste. Um mock retornando sempre sucesso
não exercita a janela de crash. Reporte separadamente testes locais e integrações reais não executadas.
