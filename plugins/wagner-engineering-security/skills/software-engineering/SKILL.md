---
name: software-engineering
description: >
  Engenharia de software para arquitetura, design de sistemas, revisão de código, refatoração,
  testes, performance, observabilidade, APIs, modelagem de domínio e decisões técnicas entre
  linguagens/frameworks. Use quando a tarefa principal for engenharia de software ampla. Não use
  como primeira opção quando o problema for especificamente Python, FastAPI, CI/CD, containers,
  pentest, AI red team ou SIEM/SOAR; nesses casos prefira a skill especializada.
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

## Recursos
- `references/architecture.md`
- `references/testing-review.md`
- `references/security-performance.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
