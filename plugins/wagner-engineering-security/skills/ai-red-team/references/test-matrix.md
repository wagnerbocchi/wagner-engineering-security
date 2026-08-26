# Matriz de testes AI/Agentic

| Área | Exemplos de teste |
|---|---|
| Prompt injection | direta, indireta, obfuscation, multi-turn |
| Data leakage | secrets, cross-tenant, RAG private docs, hidden context |
| RAG | poisoning, retrieval manipulation, malicious documents |
| Tools | unauthorized invocation, parameter injection, privilege escalation |
| Agent | planning abuse, loop/cost, unsafe autonomous action, memory poisoning |
| Output | code/HTML/SQL/shell downstream injection, unsafe rendering |
| Supply chain | model/artifact provenance, malicious adapters, dependency trust |
| Availability | unbounded consumption, token amplification, queue exhaustion |
| Governance | auditability, traceability, human approval boundaries |

Cada cenário deve ter critério de sucesso/falha explícito e ser repetível.
