# Wagner Engineering & Security

Plugin pessoal para Codex que empacota workflows técnicos de engenharia de software e segurança.

## Skills

- `software-engineering`
- `python-scripting`
- `fastapi-backend`
- `devops-cicd`
- `docker-containers`
- `networks-servers`
- `pentest-security`
- `ai-red-team`
- `detection-engineering`
- `siem-soar-development`
- `incident-response`
- `phishing-simulation`
- `startup-evaluation`

## Estrutura

```text
.agents/plugins/marketplace.json
plugins/wagner-engineering-security/
├── .codex-plugin/plugin.json
└── skills/
    └── <skill>/
        ├── SKILL.md
        └── references/
```

## Instalação pessoal no Codex

O repositório já contém um instalador cross-platform. A instalação pessoal usa:

- plugin: `~/plugins/wagner-engineering-security`
- marketplace: `~/.agents/plugins/marketplace.json`

Execute:

```bash
python scripts/install.py
```

Por padrão o instalador tenta criar um link simbólico do checkout Git para `~/plugins/` e faz fallback para cópia se o sistema não permitir symlink. Para forçar:

```bash
python scripts/install.py --mode symlink
python scripts/install.py --mode copy
```

Depois, abra/reinicie o Codex e habilite `Wagner Engineering & Security` na seção pessoal de plugins, caso ele esteja marcado apenas como `AVAILABLE`.

## Atualização em outra máquina

Se a instalação foi feita por symlink:

```bash
git pull
```

é suficiente para atualizar os arquivos do plugin. Se foi feita por cópia, rode novamente:

```bash
git pull
python scripts/install.py --mode copy
```

## Validação

```bash
python scripts/validate.py
```

O validador verifica manifestos JSON, nomes das skills, frontmatter, referências locais e termos removidos do stack legado.

## Segurança operacional

As skills ofensivas assumem uso autorizado e escopo definido. Operações destrutivas, persistência, phishing real, exfiltração ou impacto operacional devem respeitar ROE e limites explícitos do exercício.
