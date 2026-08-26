# Compose e Kubernetes

## Compose
Bom para desenvolvimento, single-host e stacks operacionais simples. Defina healthchecks, volumes,
networks e depends_on apenas quando necessário; `depends_on` não substitui readiness da aplicação.

## Kubernetes
Use quando precisa scheduling, self-healing, policy, rollout, multi-node, autoscaling ou ecossistema K8s.
Inclua requests/limits, probes, Pod Security, NetworkPolicy, PDB quando relevante e observabilidade.

A escolha deve considerar complexidade operacional total, não apenas contagem de serviços.
