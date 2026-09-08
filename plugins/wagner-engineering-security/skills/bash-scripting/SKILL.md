---
name: bash-scripting
description: >
  Use quando a tarefa principal for criar ou corrigir scripts Bash, automações Linux/cron,
  pipelines shell, quoting, sinais, locks ou reexecução após falha parcial.
  Para estruturas de dados complexas ou cliente HTTP stateful prefira python-scripting.
---

# Bash para automação operacional

Entregue em PT-BR técnico scripts completos, shell/versão exigidos, comandos de execução e códigos de
saída. Identifique Bash versus POSIX sh e ferramentas GNU/BSD; não invoque sintaxe Bash com `sh`.
No Windows, use Bash disponível/WSL explicitamente; paths e quoting de PowerShell são diferentes.

## Contrato antes de comandos

1. Defina entradas, stdout de máquina, stderr de diagnóstico e efeitos permitidos. Preserve a CLI
   existente quando possível. Para cron, declare diretório de trabalho, PATH e origem da configuração.
2. Use `"$@"`, arrays e expansões entre aspas. Passe `--` somente a comandos que o suportem e normalize
   paths quando necessário. Não use `eval`, parsing de `ls` ou loop sobre `$(find ...)` para nomes de arquivo.
3. Escolha comportamento de falha por operação: `set -euo pipefail` ajuda, mas `errexit` tem exceções
   em condições/pipelines. Capture explicitamente erros esperados e retorno das ações críticas.
4. Em enumeração, preserve delimitadores NUL; em pipeline com falha possível do produtor, capture seu
   status. Process substitution pode ocultar falha do comando produtor para o shell principal.
5. Para alteração de estado, valide todos os alvos antes da primeira mutação; resolva symlinks e
   confirme limite do diretório autorizado. Modele concorrência, interrupção e crash entre etapas.
6. Teste em diretório temporário isolado: espaços, glob literal, hífen, newline, input vazio, falha
   parcial, reexecução e sinal. Rode `bash -n`; rode ShellCheck se disponível e reporte se não estiver.

## Reexecução e operação

- `dry-run` deve impedir efeitos também nas funções auxiliares, não apenas trocar a mensagem final.
- Locks limitam concorrência no escopo que cobrem; `flock` local não cria coordenação distribuída.
- Checkpoint durável registra operação e resultado. Se o efeito ocorreu antes do checkpoint, reconcilie
  antes de repetir; `trap` não protege contra SIGKILL nem cria transação com API externa.
- Use `mktemp`, permissões restritas e cleanup apenas dos temporários criados pela execução.
  Substituição por rename exige filesystem compatível; atomicidade e durabilidade são garantias distintas.
- Não registre secrets com `set -x`; segredos não devem aparecer em argumentos/logs desnecessários.

Leia [exemplo de planejamento](references/plan-example.md) para entrada literal e execução em cron.
Troque para Python quando estado, JSON, HTTP/retries ou portabilidade tornarem Bash mais difícil de verificar.
