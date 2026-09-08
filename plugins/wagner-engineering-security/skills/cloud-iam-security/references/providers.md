# Coleta e interpretação por provider

## AWS

Correlacione identity/resource policies, trust, session policies, permissions boundaries e controles
organizacionais aplicáveis. A composição depende do principal e do tipo de concessão; siga a
[lógica oficial de avaliação](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).
Trust para assumir role e autorização da sessão resultante são etapas distintas.

## Azure / Microsoft Entra

Separe papéis de diretório, permissões da aplicação e Azure RBAC. Para RBAC, correlacione principal,
role definition, scope/herança, conditions e deny assignments aplicáveis. Acesso ao management plane
não garante nem exclui data-plane access. Consulte [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview).

## Google Cloud

Correlacione principal, bindings/roles, herança, conditions e deny policies aplicáveis. Diferencie
permissão de usar uma service account, emitir credenciais por impersonation e executar workloads sob
essa identidade. Consulte [IAM](https://docs.cloud.google.com/iam/docs/overview) e a documentação
específica da permissão antes de afirmar um caminho transitivo.

## Registro mínimo por caminho

| Campo | Evidência |
|---|---|
| Origem | Identidade e método de autenticação |
| Trust | Emissor, audience/subject e condições correspondentes |
| Destino | Role/service account/managed identity e escopo |
| Ação | Permissão, recurso e condições de contexto |
| Limites | Restrições efetivamente consultadas e políticas inacessíveis |
| Prova | Estática, simulada ou executada; data e versão da policy |

Exporte somente o material necessário e remova secrets. Para mudança, compare decisões de acesso
antes/depois com credenciais de teste autorizadas; mantenha identidade de recuperação independente.
