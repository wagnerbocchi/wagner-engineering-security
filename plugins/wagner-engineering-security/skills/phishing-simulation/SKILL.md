---
name: phishing-simulation
description: >
  Use quando a tarefa for desenhar ou avaliar simulação autorizada de phishing/social engineering: público, pretexto, infraestrutura, landing, métricas ou controles. Não aciona campanhas reais sem autorização de envio.
---

# Phishing Simulation

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

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

## Experimento e validade das métricas
- Criar material e configurar ambiente de teste não autoriza envio a participantes; respeite autorização de campanha existente sem solicitá-la novamente.
- Separe eventos de scanners/prefetch de interação humana; click/open isolados podem superestimar comportamento do participante.
- Faça tracking com identificadores opacos e acesso restrito. Não coloque e-mail, senha ou token em URL; submissão pode registrar um booleano sem transmitir o conteúdo digitado.
- Se a hipótese mede eficácia do gateway, allowlist ampla altera o experimento. Documente controles relaxados quando a campanha tiver objetivo de awareness.
- Entregue objetivo, ROE, mensagem/landing revisáveis, dry-run, stop conditions e métricas com denominadores e limitações.

## Recursos

- Para público, hipótese e interrupção: [campaign](references/campaign.md).
- Para DNS, entrega e interpretação de controles: [deliverability](references/deliverability.md).
