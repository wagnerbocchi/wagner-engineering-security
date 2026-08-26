---
name: incident-response
description: >
  Incident response e DFIR: triage, containment, eradication, recovery, evidence handling,
  threat hunting e playbooks. Use quando o objetivo principal for investigar ou responder a incidente.
  Para criar detecções use detection-engineering; para construir automação de produto use siem-soar-development.
---

# Incident Response

## Baseline
Use NIST SP 800-61 Rev. 3 e CSF 2.0 como referência atual de integração de IR com gestão de risco.
A Rev. 3 substitui a antiga Rev. 2; não trate IR como um fluxo linear rígido.

## Workflow operacional
1. Segurança imediata de pessoas/serviços e preservação de evidência compatível com o caso.
2. Triage: escopo, confiança, criticidade e impacto potencial.
3. Coleta de evidências voláteis/persistentes conforme prioridade.
4. Containment proporcional ao risco e ao efeito no negócio.
5. Investigação de root cause/attack path e hunting de extensão.
6. Eradicação e recovery com critérios de sucesso.
7. Lessons learned: detection gaps, control gaps, automation e prevenção.

## Decisões de containment
Não use regras absolutas como “nunca desligar”. Compare dano ativo, volatilidade da evidência,
capacidade de coleta, risco operacional e autoridade. Documente a decisão.

## Recursos
- `references/triage.md`
- `references/playbooks.md`
- `references/automation.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
