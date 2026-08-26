# Tuning

## Processo
1. Classifique FP por causa, não só por valor.
2. Prefira exceções estáveis e explicáveis.
3. Evite wildcard amplo que esconda atividade maliciosa.
4. Versione filtros/exceções junto com a regra.
5. Expire exceções temporárias.
6. Meça impacto antes/depois.

Métricas úteis: precision, alert volume, analyst disposition, latency, rule cost, coverage do threat model e
percentual de regras sem sinal por janela relevante. Interprete métricas no contexto.
