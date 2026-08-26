---
name: docker-containers
description: >
  Dockerfile, BuildKit, Compose, registries, imagens, runtime hardening, troubleshooting e decisão
  entre container único, Compose e Kubernetes. Use para problemas centrados em containers.
---

# Docker & Containers

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

## Recursos
- `references/docker.md`
- `references/compose-kubernetes.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
