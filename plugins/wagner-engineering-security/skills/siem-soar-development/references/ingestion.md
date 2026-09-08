# Ingestão e normalização

## Envelope mínimo
`tenant_id`, `source_id`, `event_id`, `ingested_at`, `observed_at`, `schema_version`, `raw_ref/hash`,
`parser_version`, `event_type`.

## Pipeline
receive → authenticate → rate limit → validate envelope → parse → normalize → enrich → route → persist

Preserve raw event ou hash/referência suficiente para auditoria. Normalize sem destruir campos originais
necessários para investigação.

## Autoridade, tempo e replay

- Derive tenant/source da identidade do coletor e valide vínculo com o envelope; divergência deve ser
  rejeitada/quarentenada antes de rotear ou resolver secrets. Nunca use payload externo como autoridade.
- Chave de dedupe inclui tenant e identidade estável da fonte/evento; mesmo ID em fontes distintas
  não significa duplicata. Fingerprint de conteúdo precisa de regras de canonicalização documentadas.
- Preserve timestamp original, offset conhecido, event time e ingest time. Atraso/clock skew devem ser
  observáveis; timestamp desconhecido não deve ser silenciosamente substituído sem marca de qualidade.
- Ack somente após o ponto de durabilidade definido. Documente retenção, perda tolerada e comportamento
  quando o destino não está disponível, incluindo overflow e recuperação da DLQ.
- Replay deve escolher regra/parser/enrichment históricos ou atuais explicitamente. Suprima efeitos
  externos por padrão em replay analítico; se o objetivo autorizar reexecutar ações, use política e
  identidade de operação próprias, sem colidir acidentalmente com execuções anteriores.

## Backpressure
Defina limites por tenant/source, lag metrics, retry policy e DLQ. Evite que uma fonte ruidosa degrade todo o cluster.
