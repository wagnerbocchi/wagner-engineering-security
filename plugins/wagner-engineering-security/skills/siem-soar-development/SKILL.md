---
name: siem-soar-development
description: >
  Desenvolvimento de produto SIEM/SOAR: ingestão, normalização, schema de eventos, storage/indexing,
  query/search, correlation engine, rule execution, cases, orchestration/playbooks, connectors,
  multi-tenancy, RBAC, audit, APIs, observabilidade e escala. Use quando a tarefa principal for construir
  ou evoluir uma plataforma SIEM/SOAR própria. Para escrever detecções use detection-engineering.
---

# SIEM/SOAR Product Engineering

## Perfil
Trate o usuário como engenheiro que desenvolve a própria plataforma. Priorize arquitetura implementável,
contratos claros, testes, performance, segurança multi-tenant e operabilidade.

## Arquitetura de referência
```text
Collectors/Agents -> Ingestion Gateway -> Queue/Stream -> Normalize/Enrich -> Hot storage/search
                                             |                    |
                                             v                    v
                                       replay/DLQ            detection engine
                                                                  |
                                                                  v
                                                         alerts/cases/events
                                                                  |
                                                                  v
                                                   playbook/orchestration engine
                                                                  |
                                                                  v
                                                          connectors/actions
```

## Standards e formatos úteis
- Sigma/pySigma para analytics portáveis.
- MITRE ATT&CK para comportamento/cobertura.
- OCSF e/ou ECS como inspiração de normalização, mantendo extensão controlada.
- STIX/TAXII quando integração de threat intel exigir interoperabilidade.
- OpenTelemetry para traces/metrics/logs internos do produto quando adequado.

## Requisitos não-negociáveis
- tenant isolation em storage, cache, queue, search e APIs;
- RBAC/ABAC claro e audit log imutável o suficiente para investigação;
- idempotência e dedupe em ingestão/ações;
- replay e DLQ;
- versionamento de schema e migrations;
- backpressure e quotas por tenant/source;
- connector secrets protegidos e rotacionáveis;
- playbooks com retries, timeout, compensation/rollback e human approval para ações críticas.

## Recursos
- `references/architecture.md`
- `references/ingestion.md`
- `references/orchestration.md`
- `references/testing.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
