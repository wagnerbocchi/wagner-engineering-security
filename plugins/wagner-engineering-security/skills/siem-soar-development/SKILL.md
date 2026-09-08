---
name: siem-soar-development
description: >
  Use quando a tarefa for construir ou evoluir o Sigmaward ou outra plataforma SIEM/SOAR própria: ingestão, schemas, busca, engine de correlação, cases, playbooks, connectors e isolamento multi-tenant. Para autoria de regras use detection-engineering.
---

# SIEM/SOAR Product Engineering

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

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

## Invariantes do Sigmaward
- Use Sigmaward como contexto de produto em construção, sem presumir broker, banco, cloud ou integrações existentes. Comece por contratos observados no repositório.
- Tenant vem da identidade autenticada e de contexto interno validado; rejeite divergência do envelope. Propague escopo em storage, cache, filas, busca, export e credenciais do connector.
- Defina event time, ingest time, atraso, dedupe e schema/parser version. Replay precisa indicar se reavalia regras/enrichment atuais ou reproduz versões históricas.
- Não prometa exactly-once de efeitos externos só porque a fila deduplica. Modele crash após a chamada como resultado desconhecido, com reconciliação por operação estável.
- Faça ações críticas respeitarem política/autorização do produto. Compensação pode falhar e não equivale a desfazer todo efeito.
- Entregue contrato, estados, limites por tenant, falhas exercitadas e sinais operacionais. Leia as referências apenas para o componente em mudança.

## Recursos

- Para limites dos componentes: [architecture](references/architecture.md).
- Para envelope, timestamps, replay e backpressure: [ingestion](references/ingestion.md).
- Para estados, crash recovery e connectors: [orchestration](references/orchestration.md).
- Para provar isolamento, dedupe e resiliência: [testing](references/testing.md).
