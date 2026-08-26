# Orchestration / SOAR engine

## Modelo de execução
Cada step deve ter: input schema, output schema, timeout, retry policy, idempotency key, secrets scope,
logs/traces, status e classificação de side effect.

## Estados típicos
pending → running → succeeded | failed | waiting_approval | retry_scheduled | cancelled

## Ações críticas
Suporte human approval, least privilege, dry-run quando possível, audit trail e compensation.

## Connectors
SDK de connector deve padronizar auth, pagination, rate limits, retries, errors, schemas e secret handling.
Versione connector e contract de action.
