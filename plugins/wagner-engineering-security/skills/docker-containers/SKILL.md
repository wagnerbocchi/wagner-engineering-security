---
name: docker-containers
description: >
  Use quando o problema principal for Dockerfile, BuildKit, imagem, Compose, runtime de container, volume, rede ou escolha de orquestração. Para pipeline de release use devops-cicd.
---

# Docker & Containers

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

## Workflow
1. Reproduza o problema com versão e comando exatos.
2. Inspecione build context, layers, entrypoint, env, mounts, network e healthcheck.
3. Minimize imagem e privilégios sem quebrar requisitos da aplicação.
4. Separe configuração de secret.
5. Garanta logs em stdout/stderr e health checks adequados.
6. Para produção, valide rollback e persistência antes de substituir containers.

## Hardening pragmático
- Rode como usuário não-root quando possível; UID fixo não é universal.
- Use filesystem read-only quando compatível e tmpfs para paths temporários.
- Drop capabilities e adicione somente as necessárias.
- Não monte Docker socket em workloads não confiáveis.
- Secrets via secret store/mount seguro; não em Dockerfile ou build args.
- Scaneie imagem e mantenha base atualizada.

## Orquestração
Escolha Compose, Kubernetes ou outra solução por requisitos de HA, scheduling, escala, policy,
operabilidade e experiência do time — não por número arbitrário de serviços.

## Diagnóstico e prova de operação
- Diferencie build, startup, readiness, tráfego e persistência. Verifique exit code, OOM, sinais, UID/GID e mount antes de reconstruir ou recriar.
- Compare imagem por digest e configuração efetiva. Sanitize inspect/env/logs antes de compartilhá-los; eles podem conter secrets.
- Valide SIGTERM e drain com trabalho em curso, health da aplicação e acesso a volumes com o usuário de runtime.
- Antes de substituir workload com estado, identifique volumes reais, backup/restauração e migração. Comandos como remoção de volumes não pertencem a um diagnóstico rotineiro.
- Entregue comando de reprodução, hipótese sustentada e verificação de rede, health e persistência após a mudança.

## Recursos

- Para build/runtime e coleta de sinais: [docker](references/docker.md).
- Para escolher orquestração por requisito: [compose-kubernetes](references/compose-kubernetes.md).
