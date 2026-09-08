---
name: software-engineering
description: >
  Use quando a tarefa for decisão arquitetural transversal, design de sistemas, refatoração ou revisão entre componentes/linguagens sem uma skill de domínio mais específica. Para Python, FastAPI, CI/CD, containers ou SIEM/SOAR prefira a especializada.
---

# Software Engineering

## Perfil de execução
Assuma usuário sênior e técnico. Responda em PT-BR, direto ao ponto, com trade-offs explícitos,
exemplos reais e foco em sistemas operáveis em produção. Não explique fundamentos óbvios sem necessidade.

## Entradas úteis
- Objetivo funcional e não funcional.
- Linguagem/runtime/framework e versões.
- Volume, latência, disponibilidade e consistência esperados.
- Restrições de time, prazo, custo e legado.
- Código, diagramas, logs ou métricas disponíveis.

## Workflow
1. Defina o problema e os requisitos de qualidade relevantes.
2. Identifique restrições e pontos de acoplamento.
3. Proponha a solução mais simples que preserve evolução, observabilidade e segurança.
4. Compare alternativas quando houver trade-off real.
5. Produza desenho, interfaces, código/pseudocódigo e plano de rollout quando aplicável.
6. Defina testes e sinais operacionais que provem que a mudança funcionou.

## Princípios
- Simplicidade antes de abstração prematura.
- Interfaces estáveis, internals substituíveis.
- Idempotência e contratos explícitos em integrações.
- Falhas esperadas devem ser modeladas, observadas e testadas.
- Performance deve ser medida; não otimizar por intuição.
- Segurança faz parte do design, não é etapa final.

## Saída esperada
Conforme a tarefa: ADR, diagrama textual, API contract, patch de código, plano de refatoração,
matriz de trade-offs, estratégia de testes e checklist de rollout.

## Trabalho sobre o sistema real
- Leia contratos, callers, testes e configuração antes de propor nova camada ou stack. Distinga estado atual, requisito e hipótese.
- Em bug, estabeleça reprodução e hipóteses ordenadas antes da mudança. Em refatoração, defina comportamento preservado e verificação que detecte regressão relevante.
- Declare unidade de transação e invariantes de concorrência; chamadas remotas não participam automaticamente da transação local.
- Em review, apresente achado com localização, gatilho, impacto e correção proposta. Separe risco demonstrado de melhoria opcional.
- Em produção, entregue sequência, compatibilidade, rollback e checklist pós-mudança proporcionais ao risco; mantenha alterações no fluxo de revisão autorizado.

## Recursos

- Para consistência e decisões de componentes: [architecture](references/architecture.md).
- Para revisão e verificação orientadas ao risco: [testing-review](references/testing-review.md).
- Para fronteiras de confiança e medições: [security-performance](references/security-performance.md).
