---
name: devops-cicd
description: >
  CI/CD, GitOps, Infrastructure as Code, supply-chain security, secrets, rollout e rollback.
  Use quando a tarefa principal for entrega, automação de infraestrutura ou pipeline. Não use para
  Dockerfile/Compose isolado ou arquitetura de aplicação, onde as skills específicas são melhores.
---

# DevOps & CI/CD

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

## Recursos
- `references/pipelines.md`
- `references/supply-chain.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
