---
name: fastapi-backend
description: >
  Backend com FastAPI, Pydantic v2, ASGI, APIs REST/webhooks, autenticação, persistência,
  background jobs, performance e testes. Use quando a tarefa principal envolver desenho ou
  implementação de serviço FastAPI. Para Python genérico use python-scripting; para arquitetura
  multi-serviço use software-engineering.
---

# FastAPI Backend

## Entradas úteis
- versão de Python/FastAPI/Pydantic;
- banco/ORM e estratégia de migração;
- tipo de autenticação e modelo de autorização;
- SLO de latência/throughput;
- natureza dos jobs assíncronos e garantias necessárias.

## Workflow
1. Modele contratos de API e erros antes da implementação.
2. Separe camada HTTP, domínio e infraestrutura quando o domínio justificar.
3. Defina transações, idempotência e concorrência.
4. Escolha sync/async pela natureza das dependências, não por moda.
5. Escolha execução de background por requisitos de durabilidade/retry/escala.
6. Adicione testes, health/readiness e telemetria.

## Background jobs: decisão correta
- `BackgroundTasks`: trabalho curto, best-effort, aceitável perder se o processo morrer.
- fila/worker persistente: quando precisa retry, durabilidade, escalabilidade independente, scheduling ou isolamento.
- CPU-bound: processo/worker separado; não bloquear event loop.
- Não escolher broker/worker apenas pela duração em segundos.

## Segurança
- autorização por recurso/tenant;
- validação estrita de payload;
- rate limit conforme risco;
- secrets fora do código;
- evitar SSRF em URLs controladas pelo usuário;
- limites de upload/body e timeouts.

## Recursos
- `references/architecture.md`
- `references/jobs.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
