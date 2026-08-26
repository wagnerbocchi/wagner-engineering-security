# Arquitetura e design

## Checklist de decisão
1. Quais invariantes o sistema precisa preservar?
2. Qual é a unidade de consistência/transação?
3. Onde estão os limites de confiança e os limites de falha?
4. O fluxo é síncrono, assíncrono ou híbrido?
5. Que dados precisam de replay, auditoria ou idempotência?
6. Que componente pode crescer independentemente?

## Heurísticas
- Monólito modular é frequentemente melhor ponto de partida que microserviços.
- Separe serviços quando houver limites claros de domínio, escala, ownership ou isolamento de falha.
- Use filas/eventos quando desacoplamento, durabilidade ou absorção de burst forem requisitos reais.
- Use banco relacional como default para estado transacional; escolha outro modelo por requisito, não moda.
- APIs externas devem ter timeout, retry seletivo, circuit breaker quando necessário e idempotency keys para writes repetíveis.

## ADR mínimo
- Contexto
- Decisão
- Alternativas consideradas
- Consequências positivas/negativas
- Plano de migração/reversão
