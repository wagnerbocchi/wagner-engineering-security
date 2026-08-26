# Tooling Python

## Base recomendada
```bash
uv init
uv add httpx pydantic typer
uv add --dev pytest ruff pyright
uv run ruff check .
uv run pyright
uv run pytest -q
```

Use pin/lockfile do gerenciador em vez de fixar versões arbitrárias no playbook.

## Estrutura
```text
project/
  pyproject.toml
  src/project/
    __init__.py
    cli.py
    core.py
    clients/
  tests/
```

## Async
Use async para múltiplas operações I/O concorrentes. CPU-bound deve ir para processo/worker apropriado;
não bloqueie event loop com trabalho pesado.
