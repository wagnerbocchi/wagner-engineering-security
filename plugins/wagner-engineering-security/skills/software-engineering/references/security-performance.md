# Segurança e performance por design

## Segurança
- Valide input na borda e normalize antes da lógica de negócio.
- Faça autorização no recurso/ação, não apenas na rota.
- Segredos nunca em código, imagem ou log.
- Evite construir comandos/queries com concatenação de input.
- Proteja SSRF, path traversal, deserialização insegura e chamadas de ferramentas externas.

## Performance
1. Meça p50/p95/p99 e throughput.
2. Perfil antes de otimizar.
3. Diferencie CPU, I/O, lock contention e latência de dependência.
4. Cache só com política clara de invalidação/TTL.
5. Load test deve representar distribuição realista, não apenas RPS constante.
