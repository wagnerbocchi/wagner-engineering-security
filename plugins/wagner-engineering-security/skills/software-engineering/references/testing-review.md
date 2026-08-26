# Testes e code review

## Pirâmide pragmática
- Unitários para regras puras e edge cases.
- Integração para banco, filas, cache, filesystem e provedores.
- Contract tests entre serviços.
- E2E somente para jornadas críticas.

Cobertura é sinal, não objetivo universal. Defina thresholds por criticidade e histórico do projeto.

## Code review
Procure primeiro por: correção, regressões, concorrência, tratamento de erro, segurança, observabilidade,
compatibilidade, migração de dados e operabilidade. Depois avalie estilo.

## Antes do merge
- testes relevantes passam;
- comportamento de erro foi exercitado;
- logs/metrics/traces necessários existem;
- mudança tem estratégia de rollback quando arriscada;
- documentação/contrato foi atualizado quando necessário.
