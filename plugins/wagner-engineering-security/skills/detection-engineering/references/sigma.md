# Sigma 2.1

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

Use Sigma correlation e Sigma filters quando o problema for naturalmente de correlação ou tuning compartilhado.
