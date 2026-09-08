# Avaliação das skills — expansão de perfil

O pacote passou de 13 para 19 skills. O objetivo da avaliação é verificar descoberta, referências
e aplicação das instruções a cenários compatíveis com o perfil de Wagner e o Sigmaward.

## Baseline

Uma avaliação independente leu as 13 skills originais e suas referências e respondeu aos dez cenários
abaixo, antes das alterações. Não houve falha comportamental demonstrada: as respostas empregaram
conhecimento técnico adicional para preencher omissões. As melhorias são de cobertura e orientação
operacional; não há evidência de ganho quantitativo ou causal de desempenho.

Omissões identificadas: estado de efeito externo desconhecido, outbox/inbox, semântica de atraso e
cobertura, aplicabilidade de backports, autorização em export assíncrono, IAM efetivo, freshness de
grafos AD, Bash/cron e fronteira entre código de PR e credenciais de deploy.

## Cenários reproduzíveis

Forneça os dados sintéticos e solicite uma decisão/artefato concreto; não dê ao avaliador a coluna
de critério. A avaliação é textual, sem executar ações contra ambientes reais.

| Cenário | Critério de aceitação |
|---|---|
| Worker cai após bloquear IP; redelivery com tenant divergente | Tenant rejeitado; resultado ambíguo reconciliado sem retry cego |
| Sigma compila, Image difere do campo real, 12% atrasados | Mapping e fixtures no target; política temporal; cobertura não inferida de tag |
| Scanner 9,8/backport versus 7,5 exposto e explorado | Aplicabilidade por build; prioridade contextual; fechamento com reteste |
| API GET protegido, export misto e webhook assíncrono | Autorizar toda a cadeia e validar conteúdo/efeito final com controle positivo |
| Hunt sem hits, 6h sem sensor, timestamp sem offset | Limitar conclusão; explicitar gaps e incerteza temporal |
| Trust cloud curinga, policy restrita, provider desconhecido | Separar aquisição de identidade de permissões; sem semântica universal |
| Grafo AD de 45 dias, ROE leitura | Revalidar arestas; distinguir caminho estático de exploração |
| Bash cron, paths literais e falha parcial | Quoting correto; plano sem mutação; estado/reconciliação para ações futuras |
| FastAPI publica antes de commit, POST repetido | Atomicidade outbox/idempotência e testes das janelas de crash |
| PR fork pede cache compartilhado e deploy token | Isolar código/cache/artefato não confiável de execução privilegiada |

Controles de roteamento: socket/runtime Docker → `docker-containers`; CLI Python → `python-scripting`;
pitch comercial → `startup-evaluation`; landing genérica não deve ativar `phishing-simulation`.

## Resultado após as alterações

Um segundo avaliador, em contexto independente da baseline, aplicou as novas instruções aos dez
cenários e aos quatro controles de roteamento. Produziu decisões compatíveis com os critérios e
não identificou defeitos materiais nas instruções. Sua leitura inicial encontrou o README antigo;
o catálogo foi atualizado e os links foram conferidos na versão final.

Essa passagem verifica aplicação dos casos apresentados, não generalização cega: vários exemplos
nas referências se aproximam dos cenários de avaliação. Não se atribui taxa de sucesso estatística
a uma única passagem textual, nem se confunde o plano de teste produzido com execução no alvo.

## Verificação automatizada

```bash
python scripts/validate.py
python -X utf8 -m unittest discover -s tests -v
```

Os testes usam cópias temporárias e não executam o instalador. O estado original apresentou cinco
falhas de validação nos sete testes: crescimento, diretório incompleto, descrição vazia, nome inválido
e referência quebrada dentro de outra referência. Após a correção, os sete passaram.

O validador `quick_validate.py` do `skill-creator` complementa a validação com parsing YAML, usando
PyYAML em ambiente temporário isolado. Os comandos Bash do exemplo de planejamento são verificáveis
localmente; os demais exemplos de segurança exigem os dados e ambientes de teste indicados.

Verificações executadas no checkout final:

- `validate.py`: 19 skills válidas; sete testes de regressão passaram.
- `quick_validate.py`: as 19 skills passaram no parsing YAML e nas verificações de frontmatter.
- Exemplo Bash: `bash -n` e quatro cenários executados com Git Bash — sem argumentos, apenas `--`,
  paths literais com espaço/glob/hífen/newline e lote com path relativo sem produzir plano parcial.
  O caso newline foi transportado pelo stdin do Bash para evitar conversão de argumentos Windows/MSYS.
- Exemplo Python: sintaxe compilada, sem executar chamadas HTTP.
- Links locais do catálogo/relatório e `git diff --check`: sem problemas detectados.

ShellCheck não estava disponível no ambiente e não foi executado.

## Limites

Uma aplicação textual bem-sucedida não prova robustez em múltiplos modelos, execuções ou produção.
Não se executam pentest, coleta AD/cloud, campanha de phishing ou ações SOAR reais nesta avaliação.
Não se instalam as alterações no cache de plugins nem se publicam artefatos para realizar a revisão.
