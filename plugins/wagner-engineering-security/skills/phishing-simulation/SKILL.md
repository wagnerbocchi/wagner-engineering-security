---
name: phishing-simulation
description: >
  Simulações autorizadas de phishing e social engineering para avaliação de controles e awareness:
  desenho de campanha, Gophish, landing pages seguras, deliverability, SPF/DKIM/DMARC, métricas e reporting.
  Use somente para campanhas controladas/ROE definidos.
---

# Phishing Simulation

## Princípios
- autorização, público e janela definidos;
- não coletar senha real, token ou dado sensível desnecessário;
- landing page deve registrar apenas sinais necessários para a métrica;
- estabelecer deconfliction com blue team conforme desenho do exercício;
- cleanup e retenção mínima dos dados da campanha.

## Workflow
1. Objetivo: awareness, control validation, detection, reporting ou purple team.
2. Segmentação e pretext compatíveis com ROE.
3. Domínio/email infrastructure e deliverability legítima.
4. Landing/tracking seguro.
5. Dry-run com grupo reduzido.
6. Campanha, monitoramento e stop conditions.
7. Métricas e lições aprendidas.

## Métricas
Delivery, open quando tecnicamente confiável, click, report rate, time-to-report, credential-attempt signal
sem coletar credencial, e detecção/resposta dos controles. Evite usar uma única taxa como julgamento de pessoas.

## Recursos
- `references/campaign.md`
- `references/deliverability.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
