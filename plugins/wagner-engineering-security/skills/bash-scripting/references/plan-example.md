# Planejamento local sem alteração de arquivos

Exemplo Bash, não POSIX sh. Aceita caminhos absolutos já fornecidos pelo operador; apenas imprime
um plano. Não resolve symlinks, comprova existência nem implementa ações ou idempotência remota.
Valida todos os argumentos antes de emitir o plano, evitando plano parcial por input inválido.

```bash
#!/usr/bin/env bash
set -euo pipefail
export PATH=/usr/bin:/bin
export LC_ALL=C
umask 077

if [[ ${1-} == -- ]]; then
  shift
fi
if (($# == 0)); then
  printf 'uso: plan.sh -- /caminho/absoluto [...]\n' >&2
  exit 64
fi

paths=("$@")
for target in "${paths[@]}"; do
  if [[ $target != /* ]]; then
    printf 'caminho deve ser absoluto: %q\n' "$target" >&2
    exit 64
  fi
done

for target in "${paths[@]}"; do
  printf 'PLAN path=%q\n' "$target"
done
```

Salve como `plan.sh` e execute com Bash instalado:

```bash
bash -n plan.sh
bash plan.sh -- '/lab/com espaço' '/lab/*' '/lab/-arquivo'
```

Aspas no chamador são necessárias: glob expandido antes de chegar ao script não pode ser reconstruído.
`%q` oferece representação legível/reutilizável em Bash, não é serialização universal para outras shells.
Em cron, use caminho absoluto para o interpretador e script; configure destinatário/log de falhas.

Ao adaptar para mutações, acrescente validação canônica de alvo, limite autorizado, chave de operação,
checkpoint, controle de concorrência e reconciliação proporcionais ao efeito. Não acrescente esses
mecanismos ao modo de impressão quando não há estado para proteger.
