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
