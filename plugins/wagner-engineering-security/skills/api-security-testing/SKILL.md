---
name: api-security-testing
description: >
  Use quando a tarefa for testar segurança de APIs REST, GraphQL ou webhooks: BOLA/IDOR,
  autorização entre tenants, funções privilegiadas, exports assíncronos, SSRF ou lógica de negócio.
  Para implementar serviço FastAPI use fastapi-backend; para campanha ofensiva ampla use pentest-security.
---

# Segurança de APIs

Produza prova reproduzível no escopo autorizado, em PT-BR técnico. Reaproveite ROE, contas e limites
já informados; a existência de uma credencial não amplia seu escopo. Trabalhe com recursos sintéticos
e evidência mínima. Descoberta de endpoints não autoriza testar terceiros encontrados em respostas.

## Fluxo de avaliação

1. Identifique contrato real: endpoints/versões, métodos, identidade, tenant, objeto, papel e estado.
   Compare OpenAPI/GraphQL schema com tráfego e código disponíveis; documentação pode omitir rotas.
2. Monte matriz identidade × objeto × ação × tenant com controles positivos e negativos.
   Teste autorização horizontal, vertical e em propriedades, incluindo listas, busca, bulk e exports.
3. Siga operações assíncronas até o efeito: job, worker, storage, URL de download e webhook.
   Verifique a política para acesso revogado entre submissão e execução/entrega.
4. Para authn, verifique issuer/audience, expiração, rotação e revogação conforme o mecanismo real.
   Token decodificado não comprova assinatura validada. Autenticação bem-sucedida não prova authz.
5. Exercite replay, concorrência e limites com orçamento de requisições definido pelo ambiente.
   Em webhooks, valide assinatura sobre bytes corretos, freshness, dedupe e tratamento de retry.
6. Reteste a correção com a mesma prova e com um fluxo autorizado que deve continuar funcionando.

## Decisões que mudam a prova

| Superfície | Evidência necessária |
|---|---|
| BOLA/IDOR | Conteúdo/efeito de objeto alheio; status HTTP isolado é insuficiente |
| Bulk/export | IDs mistos, autorização por item e artefato final, incluindo callback |
| SSRF | Destino controlado no laboratório; validar redirects e resolução, sem sondar redes fora do escopo |
| GraphQL | Autorização em resolver/nó e limites de aliases, batching e custo conforme runtime |
| Mass assignment | Campo privilegiado efetivamente alterado, com snapshot antes/depois |

## Entrega

Por finding: precondição, request sanitizada, expected/actual, IDs de correlação, impacto demonstrado,
correção na fronteira responsável e reteste. Registre casos inconclusivos quando worker/storage não
estiverem acessíveis. Não publique tokens, cookies ou dados reais como evidência.

Leia [matriz de exportação](references/authorization-matrix.md) ao testar BOLA em jobs e callbacks.
Use [OWASP API Security](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) como taxonomia;
registre a edição consultada e não trate o Top 10 como cobertura exaustiva.
