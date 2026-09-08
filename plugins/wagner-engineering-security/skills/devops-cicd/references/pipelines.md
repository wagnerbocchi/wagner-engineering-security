# Pipelines

## Stages típicos
validate → test → security → build → attest/sign → deploy staging → smoke → promote prod → verify

Não force todos os stages em todo projeto. Use matriz de risco.

## Deploy seguro
- artefato imutável por digest/version;
- migration compatível com rollout/rollback;
- canary/blue-green quando o risco justificar;
- health e SLI/SLO durante rollout;
- rollback automatizável e ensaiado.

## Código não confiável

PR/fork executa testes sem secrets de deploy, identidade cloud privilegiada ou runner persistente
com acesso a produção. Isole/desabilite caches graváveis por essa origem; não reutilize seus artefatos
como executáveis de um job privilegiado sem estabelecer confiança na origem e no processo de build.

Em GitHub Actions, avalie especialmente eventos/contextos privilegiados e checkout de código do PR:
permissão do workflow e origem do código executado são decisões separadas. Verifique a semântica atual
na documentação oficial antes de gerar YAML; nome de evento sozinho não prova isolamento.

## Checklist pós-mudança crítica

- Commit, digest, ambiente e identidade de execução correspondem ao release autorizado.
- Readiness, fluxo crítico, dependências e migração operam com versões coexistentes.
- Erros, latência, backlog e isolamento observados no intervalo definido.
- Critério de abortar e rollback/recuperação de dados disponíveis.
