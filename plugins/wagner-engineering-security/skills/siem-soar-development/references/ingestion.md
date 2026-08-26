# Ingestão e normalização

## Envelope mínimo
`tenant_id`, `source_id`, `event_id`, `ingested_at`, `observed_at`, `schema_version`, `raw_ref/hash`,
`parser_version`, `event_type`.

## Pipeline
receive → authenticate → rate limit → validate envelope → parse → normalize → enrich → route → persist

Preserve raw event ou hash/referência suficiente para auditoria. Normalize sem destruir campos originais
necessários para investigação.

## Backpressure
Defina limites por tenant/source, lag metrics, retry policy e DLQ. Evite que uma fonte ruidosa degrade todo o cluster.
