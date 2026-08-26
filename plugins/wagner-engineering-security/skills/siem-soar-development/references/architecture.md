# Arquitetura SIEM/SOAR

## Componentes
- ingestion gateway: auth, quotas, parsing envelope;
- stream/queue: buffering, partitioning, replay;
- normalizer/enricher: schema mapping e context enrichment;
- hot search: investigação e dashboards;
- cold/archive: retenção econômica;
- detection engine: stateless + correlation/stateful;
- alert/case service;
- orchestration engine;
- connector runtime;
- identity/tenant/audit service.

Separe control plane de data plane quando escala, segurança ou isolamento operacional justificarem.
