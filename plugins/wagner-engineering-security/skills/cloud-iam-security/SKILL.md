---
name: cloud-iam-security
description: >
  Use quando a tarefa principal for revisar IAM cloud, federação OIDC, workload identities,
  permissões efetivas, trust entre contas/projetos ou caminhos de escalada por políticas.
  Para entrega de infraestrutura use devops-cicd; para pentest amplo use pentest-security.
---

# IAM e fronteiras de confiança em cloud

Trabalhe em PT-BR técnico. Identifique provider, organização, conta/subscription/projeto, identidade
de coleta e escopo autorizado. Comece com exports/policies e consultas de leitura. Reutilize autorização
existente; uma avaliação de IAM não autoriza assumir identidades ou modificar políticas por si só.

## Perguntas de análise

1. Quem pode obter a identidade? Inspecione issuer, audience, subject/claims, condições, origem da
   federação e caminhos indiretos de impersonation/delegação. Wildcard requer avaliar quem ele inclui.
2. O que ela pode fazer? Correlacione actions, resources, conditions, bindings herdados, políticas de
   recurso e mecanismos de restrição do provider. Role com nome “Reader” não substitui sua definição.
3. Há acesso transitivo? Verifique capacidade de alterar políticas, passar/impersonar identidades,
   ler secrets, modificar workloads ou acionar pipelines privilegiados, conforme evidência disponível.
4. A conclusão reflete contexto real? Considere sessão, claims, tags, rede e escopo; ausência de acesso
   do coletor a uma política é lacuna, não evidência de ausência de permissão.
5. Qual correção preserva o fluxo legítimo? Proponha redução de trust, actions/resources e condições
   com comparação de chamadas necessárias. Teste identidade autorizada e identidade que deve ser negada.

## Modelo de evidência

```text
principal de origem -> emissão/claims -> trust -> identidade efetiva
-> ação + recurso + condições -> decisão conforme políticas aplicáveis
```

Trust federado amplo com acesso restrito a um bucket pode expor os dados desse bucket; não prova
administração de toda a cloud. Separe resultado de simulador, inferência estática e ação realmente
executada. Registre quando o simulador não representa todos os mecanismos de autorização.

## Mudança e entrega

Entregue caminho de acesso, policies/IDs e timestamps, precondições, confiança, impacto e patch mínimo.
Se a alteração for autorizada, salve configuração anterior e plano de recuperação, aplique no escopo
definido e valide novo token/sessão, fluxo legítimo, negativa e auditoria. Considere propagação e sessões
existentes antes de declarar revogação concluída.

Leia [semântica por provider](references/providers.md) apenas para a cloud identificada. Não replique
a lógica de avaliação de AWS como se fosse universal para Azure e GCP.
