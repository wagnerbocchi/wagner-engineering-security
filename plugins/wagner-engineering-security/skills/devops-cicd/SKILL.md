---
name: devops-cicd
description: >
  Use quando a tarefa principal for pipeline CI/CD, GitOps, IaC, build/proveniência ou rollout de infraestrutura. Para Dockerfile/Compose isolado use docker-containers; para avaliação de permissões cloud use cloud-iam-security.
---

# DevOps & CI/CD

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

## Workflow
1. Identifique SCM, runner, ambientes e restrições de deploy.
2. Garanta build reproduzível e artefato imutável.
3. Execute testes e scans proporcionais ao risco.
4. Gere/proteja provenance, SBOM e assinatura quando necessário.
5. Promova o mesmo artefato entre ambientes.
6. Defina rollout, observabilidade e rollback testado.

## Princípios
- Pipeline é código, versionado e revisado.
- Thresholds de coverage, duração e rollback são metas do contexto, não constantes universais.
- Secrets devem vir de secret manager/OIDC quando possível; evite credenciais long-lived.
- Dependências e actions devem ser pinadas de forma verificável.
- Produção requer evidência de deploy: commit, artefato, ator, horário, ambiente e resultado.

## Ferramentas usuais
GitHub Actions, GitLab CI, Jenkins, Terraform/OpenTofu, Ansible, Pulumi, Argo CD, Flux,
Helm, Kustomize, SOPS, Vault, External Secrets, Trivy, Grype, Semgrep, Checkov, Syft, Cosign.

## Fronteiras de execução e promoção
- Separe código de PR/fork não confiável de jobs com secrets, OIDC privilegiado ou runners persistentes. Cache e artefatos também atravessam essa fronteira; origem não confiável não deve alimentar execução privilegiada sem validação apropriada.
- Vincule identidade federada ao repositório/ref/ambiente e ao evento autorizado. Um token curto ainda pode ter privilégios excessivos.
- Faça promoção pelo digest e proveniência verificados, incluindo origem do build. Assinatura válida de artefato contaminado não comprova build confiável.
- Em migração de dados, compare expand/contract e rollout coordenado. Reverter imagem não desfaz schema incompatível ou perda de dados.
- Respeite a branch e o fluxo de revisão solicitados. Implementar uma pipeline não autoriza push, merge, deploy ou publicação por conta própria.

## Recursos

- Para desenho do fluxo e validação pós-deploy: [pipelines](references/pipelines.md).
- Para identidade, dependências e artefatos: [supply-chain](references/supply-chain.md).
