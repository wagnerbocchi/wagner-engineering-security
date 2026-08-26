# Detection as Code

```text
detections/
  rules/
  correlations/
  filters/
  tests/
  fixtures/
  mappings/
```

CI recomendada:
1. schema/lint;
2. IDs duplicados;
3. tests positivos/negativos;
4. compile/conversion para targets suportados;
5. policy checks de metadata;
6. diff de regras e impacto esperado;
7. deploy controlado.

Mantenha versão do compiler/backend para tornar resultados reproduzíveis.
