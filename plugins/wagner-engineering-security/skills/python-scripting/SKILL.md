---
name: python-scripting
description: >
  Use quando a tarefa principal for script, CLI ou automação Python: parsing, processamento de dados, integração HTTP, concorrência ou ferramenta interna. Para serviço FastAPI completo use fastapi-backend; para avaliação ofensiva use a skill de segurança pertinente.
---

# Python Scripting & Automation

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

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

## Falhas e contratos de automação
- Reutilize gerenciador, dependências e convenções do projeto; um script stdlib não exige novo framework de CLI ou migração para uv.
- Diferencie timeout de conexão de resultado remoto desconhecido. Retry de write exige garantia da operação/provider e reconciliação quando o resultado é ambíguo.
- Feche clients/streams, limite concorrência e propague cancelamento. Streaming e paginação precisam de limites de memória e detecção de cursor repetido.
- Trate subprocess com argumentos separados, timeout e retorno explícito; credenciais não devem aparecer em logs ou mensagens de exceção.
- Valide input malformado, página vazia/repetida, 429/timeout, redelivery e códigos de saída pertinentes. Preserve stdout de máquina e envie diagnóstico a stderr.

## Recursos

- Para escolher tooling compatível com o projeto: [tooling](references/tooling.md).
- Para HTTP, idempotência e retry: [automation](references/automation.md).
