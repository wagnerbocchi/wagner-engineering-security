---
name: detection-engineering
description: >
  Use quando a tarefa for criar, revisar, testar ou ajustar detecções Sigma/pySigma, correlações e analytics com fixtures e backend definido. Para investigação proativa use threat-hunting; para implementar a engine use siem-soar-development.
---

# Detection Engineering

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

## Baseline
Prefira Sigma quando a detecção puder ser expressa de forma portátil. Registre versões da especificação,
pySigma, backend e processing pipeline realmente suportadas. Correlation/filters dependem dessas
capacidades. O backend final pode ser query DSL, SQL, Lucene-like, streaming CEP ou engine própria.

## Workflow
1. Hipótese de detecção e comportamento adversário.
2. Data source e campos necessários.
3. Samples positivos, negativos e de borda.
4. Regra/analytic e mapeamento ATT&CK.
5. Test bench/replay.
6. Tuning e exceptions controladas.
7. Deploy via detection-as-code.
8. Medir precisão, latência, custo e cobertura relevante.

## Qualidade
Uma detecção madura deve ter owner, versão, status, data source, rationale, ATT&CK quando aplicável,
fixtures de teste, known false positives, query target e revisão periódica.

Não use quotas universais de FPR, MTTD ou coverage. Defina SLOs por threat model, criticidade, fonte de dados
e capacidade operacional.

## Semântica e cobertura comprovada
- Inspecione eventos reais sanitizados e o schema: campo, tipo, null/missing, case e escaping. Declare o mapping de Sigma até o campo efetivamente consultado no backend.
- Compilar uma regra não prova detecção: execute fixtures positiva, benigna e de borda no target, ou entregue a execução como pendente quando ele não estiver disponível.
- Diferencie event time de ingest time. Em correlação, explicite chave de agrupamento com tenant, janela, atraso permitido, reordenação e dedupe; dimensione lookback com dados de atraso.
- Tag ATT&CK descreve intenção. Registre separadamente fonte disponível, analytic testado e operação monitorada; não derive cobertura apenas contando tags.
- Entregue regra/query, versão de compiler/backend/pipeline, fixtures e resultado observado; exceções devem ter owner, justificativa e revisão.

## Recursos

- Para mapping e execução no backend: [sigma](references/sigma.md).
- Para analisar ruído e exceções: [tuning](references/tuning.md).
- Para versionamento, testes e promoção de regras: [detection-as-code](references/detection-as-code.md).
