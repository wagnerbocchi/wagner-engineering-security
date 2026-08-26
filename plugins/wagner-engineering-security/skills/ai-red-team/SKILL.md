---
name: ai-red-team
description: >
  AI red teaming e segurança de LLM/GenAI/agentic systems: prompt injection direta/indireta,
  jailbreaks, RAG poisoning, data leakage, system prompt leakage, tool abuse, excessive agency,
  memory/context poisoning, model abuse, supply chain e avaliações adversariais. Use quando o alvo
  principal incluir modelo, RAG, agente, MCP/tool calling ou aplicação GenAI. Para pentest tradicional,
  use pentest-security.
---

# AI Red Team

## Baseline 2026
Use como referências primárias: OWASP GenAI LLM Top 10 2026, OWASP Top 10 for Agentic Applications 2026,
OWASP GenAI Red Teaming Guide e MITRE ATLAS. ATLAS deve ser usado para mapear técnicas quando útil.

## Escopo de avaliação
1. Modelo: comportamento, jailbreaks, model extraction/misuse, harmful capability conforme escopo.
2. Aplicação: prompt assembly, output handling, authz, secrets, RAG, plugins/tools.
3. Infra: endpoints, storage, model gateway, queues, CI/CD e supply chain.
4. Runtime: agente, memória, tool calling, data exfiltration, privilege boundaries e cost abuse.

## Workflow
1. Defina sistema, modelo, providers, tools, data stores, trust boundaries e impacto permitido.
2. Faça threat model por OWASP + MITRE ATLAS.
3. Monte corpus de testes reproduzível com IDs e expected behavior.
4. Execute manual + automatizado; preserve prompts, outputs, traces e tool calls.
5. Diferencie vulnerabilidade, safety failure, reliability failure e configuração insegura.
6. Reteste mitigação e meça regressão de utilidade.

## Ferramentas usuais
`garak`, Microsoft PyRIT, `promptfoo`, Giskard, Inspect AI, scripts Python, proxies HTTP,
LM Studio/Ollama para labs locais e harnesses próprios para agents/RAG. Escolha por cobertura e
reprodutibilidade, não por quantidade de payloads.

## Métricas
Attack Success Rate (ASR), pass/fail por cenário, severidade de impacto, reproducibility rate,
false-positive/false-negative do guardrail, token/cost amplification e regressão de qualidade.

## Recursos
- `references/methodology.md`
- `references/tools.md`
- `references/test-matrix.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
