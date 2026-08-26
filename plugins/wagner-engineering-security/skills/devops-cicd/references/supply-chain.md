# Supply-chain security

- gere SBOM (CycloneDX/SPDX) no build;
- escaneie dependências e imagem;
- assine artefatos quando o ambiente exigir confiança verificável;
- prefira OIDC/workload identity a secrets long-lived em CI;
- fixe actions/plugins por versão/digest confiável;
- proteja branch/tag de release;
- mantenha provenance e trilha de auditoria.

Ferramentas comuns: Syft, Grype, Trivy, Cosign/Sigstore, Gitleaks, Semgrep, Checkov.
