# Wagner Engineering & Security

Plugin pessoal para Codex com 19 skills de engenharia e cibersegurança, orientadas ao trabalho de
Wagner Bocchi na Bocchi Company e ao desenvolvimento do Sigmaward, seu SIEM/SOAR próprio.

As instruções assumem interlocutor técnico, respostas em PT-BR, evidência reproduzível, hipóteses
ordenadas em troubleshooting e trade-offs explícitos. Sigmaward é contexto de produto: as skills
não presumem banco, broker, cloud ou integrações já implantadas.

## Skills

Escolha pelo objetivo principal. Uma linguagem, framework ou ferramenta citada incidentalmente não
deve ativar todas as skills relacionadas. Cada entrada aponta para referências condicionais.

| Skill | Quando usar |
|---|---|
| [software-engineering](plugins/wagner-engineering-security/skills/software-engineering/SKILL.md) | Arquitetura transversal, refatoração e revisão |
| [python-scripting](plugins/wagner-engineering-security/skills/python-scripting/SKILL.md) | Scripts, CLIs, parsing e integrações Python |
| [bash-scripting](plugins/wagner-engineering-security/skills/bash-scripting/SKILL.md) | Shell, cron, quoting, falha parcial e reexecução |
| [fastapi-backend](plugins/wagner-engineering-security/skills/fastapi-backend/SKILL.md) | Serviço ASGI, contratos, persistência e jobs |
| [devops-cicd](plugins/wagner-engineering-security/skills/devops-cicd/SKILL.md) | Pipelines, IaC, proveniência e rollout |
| [docker-containers](plugins/wagner-engineering-security/skills/docker-containers/SKILL.md) | Build, runtime, Compose e volumes |
| [networks-servers](plugins/wagner-engineering-security/skills/networks-servers/SKILL.md) | DNS, TLS, rede e serviços Linux/Windows |
| [pentest-security](plugins/wagner-engineering-security/skills/pentest-security/SKILL.md) | Avaliação ofensiva ampla e exploração controlada |
| [api-security-testing](plugins/wagner-engineering-security/skills/api-security-testing/SKILL.md) | BOLA, autorização, exports, webhooks e lógica de negócio |
| [active-directory-security](plugins/wagner-engineering-security/skills/active-directory-security/SKILL.md) | ACLs, grupos, delegação, AD CS e caminhos de ataque |
| [cloud-iam-security](plugins/wagner-engineering-security/skills/cloud-iam-security/SKILL.md) | Trust, federação e permissões efetivas em cloud |
| [vulnerability-management](plugins/wagner-engineering-security/skills/vulnerability-management/SKILL.md) | Aplicabilidade, backports, prioridade, exceções e fechamento |
| [ai-red-team](plugins/wagner-engineering-security/skills/ai-red-team/SKILL.md) | LLM, RAG, agentes, MCP e avaliações adversariais |
| [threat-hunting](plugins/wagner-engineering-security/skills/threat-hunting/SKILL.md) | Hipóteses proativas, pivôs e cobertura da telemetria |
| [detection-engineering](plugins/wagner-engineering-security/skills/detection-engineering/SKILL.md) | Regras Sigma, correlação, replay e tuning |
| [siem-soar-development](plugins/wagner-engineering-security/skills/siem-soar-development/SKILL.md) | Engine, ingestão, multi-tenancy, cases e connectors do produto |
| [incident-response](plugins/wagner-engineering-security/skills/incident-response/SKILL.md) | Incidente em curso, evidência, containment e recuperação |
| [phishing-simulation](plugins/wagner-engineering-security/skills/phishing-simulation/SKILL.md) | Campanha autorizada e avaliação de controles/awareness |
| [startup-evaluation](plugins/wagner-engineering-security/skills/startup-evaluation/SKILL.md) | Hipótese de negócio, piloto, adoção e viabilidade |

## Exemplos de uso

```text
Use $siem-soar-development para revisar o retry do connector do Sigmaward:
o provider executa a ação, mas o worker pode cair antes de salvar o resultado.

Use $api-security-testing para montar testes de isolamento entre tenants
na exportação assíncrona de casos, usando fixtures e receptor de webhook de laboratório.

Use $vulnerability-management para triar estes findings, validar backports
e definir prioridade, owner, evidência de correção e reteste.

Use $threat-hunting para investigar esta hipótese nos logs fornecidos,
registrando gaps, qualidade temporal e limites de uma conclusão sem hits.

Use $bash-scripting para corrigir este job cron preservando nomes de arquivos
com espaços e tornando explícito o comportamento após falha parcial.
```

Para objetivo composto, combine as especialidades necessárias: `threat-hunting` investiga a hipótese,
`detection-engineering` transforma evidência em regra e `siem-soar-development` implementa a execução
na plataforma. O uso de uma skill não pressupõe a disponibilidade de ferramentas externas.

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
python -X utf8 -m unittest discover -s tests -v
```

O validador usa somente a biblioteca padrão e descobre skills sem contagem fixa. Verifica manifestos
JSON, nomes, frontmatter no formato usado pelo pacote, descrições, referências locais e termos removidos
do stack legado. Ele não substitui parser YAML completo nem prova qualidade das decisões do agente.

Os testes exercitam crescimento do catálogo, diretório incompleto, descrição vazia, nome inválido e
referências ausentes. Veja [cenários de avaliação](docs/skill-validation.md) para os limites da validação
comportamental. Nenhuma validação requer acesso a produção.

## Segurança operacional

As skills ofensivas assumem uso autorizado e escopo definido. Operações destrutivas, persistência, phishing real, exfiltração ou impacto operacional devem respeitar ROE e limites explícitos do exercício.
