---
name: incident-response
description: >
  Use quando a tarefa principal for triar, investigar, conter ou recuperar um incidente de segurança e preservar evidência DFIR. Para hunt proativo sem incidente confirmado use threat-hunting; para implementar playbooks no produto use siem-soar-development.
---

# Incident Response

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

## Baseline
Use [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) e CSF 2.0 como
referência de integração de IR com gestão de risco; confirme a edição ao citar requisitos atuais.
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

## Registro operacional e encerramento
- Mantenha timeline com fonte, timestamp original, UTC normalizado, incerteza de relógio, evidência e confiança. Registre o que é observado e o que é hipótese.
- Em coleta, documente host/identidade, ferramenta, horário, hash e acesso; trabalhe sobre cópia quando possível. Hash comprova integridade relativa, não a veracidade da origem.
- Para cada containment, registre escopo, motivo, autoridade já existente, efeito esperado, risco operacional e reversibilidade. Não peça novamente autorização coberta pelo contexto.
- Verifique credenciais/sessões, persistência e alcance conforme evidência. Patching isolado não prova erradicação; recuperação exige serviço funcional e monitoramento dos sinais relevantes.
- Entregue status, impacto, evidências, decisões, pendências e critério de próxima atualização; prepare comunicações sem enviá-las sem autorização.

## Recursos

- Para coleta inicial e prioridade: [triage](references/triage.md).
- Para ramificações e critérios de resposta: [playbooks](references/playbooks.md).
- Para implementar steps auditáveis e repetíveis: [automation](references/automation.md).
