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
