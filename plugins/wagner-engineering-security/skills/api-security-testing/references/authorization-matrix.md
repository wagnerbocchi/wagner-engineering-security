# Exportação entre tenants: fixture de laboratório

Contexto: identidades `user_a`/`user_b`, casos sintéticos `case_a`/`case_b` e receptor de webhook
controlado. Cada recurso tem um marcador exclusivo para detectar vazamento sem usar informação real.
Escolha a semântica documentada de lote: rejeição integral ou resultado parcial autorizado.

| Identidade | Operação | Resultado esperado |
|---|---|---|
| A | GET case_a | Dados de A |
| A | GET case_b | Negado, sem conteúdo de B |
| A | POST export [case_a] | Job e arquivo de A |
| A | POST export [case_b] | Nenhum dado ou efeito de B |
| A | POST export [case_a, case_b] | Rejeição integral, ou parcial sem B se esse for o contrato |
| B | Consultar job/baixar export de A | Negado, incluindo URL direta conforme política |
| A revogado após submit | Executar/entregar export | Política de revogação aplicada e auditada |

Compare submissão, poll do job, bytes do arquivo, destinatário e callback. Um `403` no GET não
valida o worker. Um `202` no POST não prova sucesso nem vulnerabilidade.

Exemplo de caso de teste a adaptar ao cliente/fixtures existentes:

```text
setup: criar case_a(marker=A_ONLY), case_b(marker=B_ONLY)
ação: user_a solicita export [case_a, case_b]
aguardar: conclusão observável com deadline, sem sleep fixo
assert: B_ONLY ausente de resposta, status, arquivo, callback e logs acessíveis a A
controle: user_a exporta case_a e recebe A_ONLY
cleanup: remover apenas recursos sintéticos criados pelo teste
```

Na correção, derive tenant da identidade autenticada; transporte contexto confiável até o worker.
Resolva IDs com tenant e ação, aplique autorização por objeto e valide destino de entrega.
URL assinada é uma capacidade: documente validade, compartilhamento e limites de revogação reais.
