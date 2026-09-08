# Registro de hunt

Preencha apenas com informação observada; use `desconhecido` em vez de completar evidência por inferência.

```yaml
hunt_id: HUNT-LAB-001
hypothesis: Uso anômalo de conta de serviço fora dos hosts esperados
scope:
  tenant: lab-a
  population: contas de serviço do laboratório
  window: intervalo com início/fim e timezone explícitos
telemetry:
  sources: fontes realmente consultadas
  coverage: ativos/fontes presentes e ausentes
  gaps: intervalos sem coleta, retenção ou campos necessários
  time_quality: offset comprovado, clock skew e atraso conhecidos
query:
  engine: mecanismo e versão utilizados
  artifact: caminho da consulta executada e parâmetros
  positive_control: evento conhecido recuperado ou motivo da ausência
observations:
  hits: contagem realmente obtida
  evidence: IDs/artefatos com proveniência e acesso restrito
  alternatives: explicações benignas verificadas e pendentes
conclusion:
  status: inconclusiva
  reasoning: relação entre evidência e hipótese
  next_action: próxima coleta/consulta ou handoff para IR
```

Exemplo de inferência válida: “Nenhum hit nas 18h com dados disponíveis; as outras 6h não foram
avaliadas. Timestamps sem offset impedem ordenar eventos dessas fontes com precisão.”

Para converter o hunt em detecção, entregue comportamento, campos necessários, fixtures positiva/negativa,
janela e condições de falsa correspondência. O autor da regra deve validar a semântica no backend real.
