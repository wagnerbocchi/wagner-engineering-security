---
name: python-scripting
description: >
  Python para automação, CLIs, integrações HTTP, parsing, processamento de dados, concorrência,
  testes e ferramentas internas. Use quando Python for o meio principal da solução. Não use para
  ofensiva/pentest, AI red team ou backend FastAPI completo; prefira as skills especializadas.
---

# Python Scripting & Automation

## Defaults preferidos
- Python moderno com `pyproject.toml`.
- `uv` ou ferramenta equivalente para ambientes e lockfile.
- `ruff` para lint/format; `pyright` ou `mypy` conforme o projeto.
- `pytest` para testes.
- `httpx` para HTTP; `pydantic` para validação quando útil; `typer` para CLI rica.
- `asyncio` somente quando houver ganho real de concorrência I/O.

## Workflow
1. Defina contrato de entrada/saída e modo de execução: script, CLI, library ou worker.
2. Modele erros esperados e códigos de saída.
3. Implemente timeout e retry seletivo em I/O externo.
4. Use logging estruturado; preserve stdout para output de máquina quando apropriado.
5. Escreva testes dos caminhos críticos e casos de erro.
6. Produza instruções reproduzíveis de execução.

## Padrões
- `subprocess.run([...], check=True)` em vez de shell string quando possível.
- Nunca use `eval()` ou deserialização insegura em input não confiável.
- Idempotência para automações que criam/alteram estado remoto.
- Paginação, rate limit e backoff explícitos em APIs.
- Tipos e dataclasses/Pydantic devem reduzir ambiguidade, não burocracia.

## Saída esperada
Código completo ou patch, comandos de setup/run/test, estrutura de arquivos quando relevante,
e notas de operação/observabilidade.

## Recursos
- `references/tooling.md`
- `references/automation.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
