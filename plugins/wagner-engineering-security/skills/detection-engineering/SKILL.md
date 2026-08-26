---
name: detection-engineering
description: >
  Engenharia de detecção vendor-neutral: hipóteses, Sigma, pySigma, correlação, MITRE ATT&CK,
  data-source coverage, tuning, detection-as-code, testes e métricas de qualidade. Use para criação,
  revisão e evolução de detecções. Para arquitetura do produto SIEM/SOAR use siem-soar-development;
  para resposta a incidentes use incident-response.
---

# Detection Engineering

## Baseline
Prefira Sigma quando a detecção puder ser expressa de forma portátil. Considere a especificação Sigma
2.1.0 e recursos de correlation/filters quando apropriados. O backend final pode ser query DSL, SQL,
Lucene-like, streaming CEP ou engine própria.

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

## Recursos
- `references/sigma.md`
- `references/tuning.md`
- `references/detection-as-code.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
