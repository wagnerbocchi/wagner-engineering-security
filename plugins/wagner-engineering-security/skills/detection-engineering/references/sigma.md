# Sigma e semântica do backend

## Campos essenciais de regra
`title`, `logsource`, `detection` e metadados úteis como `id`, `status`, `description`, `references`,
`author`, `date`, `modified`, `falsepositives`, `level`, `tags`.

Use UUID estável; nova lógica material pode justificar novo ID e relacionamento `related`.

## Validação
- lint/schema;
- fixture positiva;
- fixture negativa;
- conversão pelo backend/pySigma;
- execução no target quando disponível.

Use Sigma correlation e Sigma filters quando o problema for naturalmente de correlação ou tuning compartilhado
e o backend suportar os recursos usados. Registre versões e limitações explicitamente.

## Mapping e replay

Exemplo: regra usa `Image`, mas o evento normalizado contém `process.executable`. Verifique o pipeline de
transformação e o significado do campo antes de mudar a regra. Não invente nome de backend do Sigmaward.

| Fixture | Prova |
|---|---|
| Comportamento adversário sintético | Match na query executada no target |
| Processo benigno semelhante | Não corresponde à lógica adversária |
| Campo ausente/null e case diferente | Semântica esperada de null/case |
| Evento atrasado/fora de ordem | Janela e atraso permitidos explícitos |
| Redelivery e outro tenant | Sem alerta duplicado nem correlação entre tenants |

Execução de `cmd.exe` sozinha pode testar o pipeline de dados, mas não prova técnica adversária.
Registre os resultados esperados/observados, artefato da query e versões. Use a documentação de
[backends Sigma](https://sigmahq.io/docs/digging-deeper/backends.html) para verificar conversão disponível;
sucesso de conversão não substitui replay no mecanismo de consulta.
