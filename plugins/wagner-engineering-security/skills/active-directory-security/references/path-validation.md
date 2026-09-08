# Revalidar um caminho sem executar exploração

Exemplo: export BloodHound com 45 dias, escopo permite apenas leitura.

```text
edge_id | principal SID/DN | relação | objeto SID/DN
fonte | collected_at | revalidated_at | precondição | confiança
```

Comece pela aresta de maior impacto e confirme existência/estado de objetos e membros/ACLs atuais.
Documente mudanças desde o export; um caminho quebrado invalida aquela sequência, não todas as
possibilidades de ataque. Não execute ações propostas por uma ferramenta só para confirmar a visualização.

Leituras pontuais com módulo ActiveDirectory/RSAT, quando instalado e permitido:

```powershell
Get-ADDomain | Select-Object DNSRoot, DomainSID, DomainMode
Get-ADGroup -Identity 'GG-Lab-Operators' -Properties member, whenChanged |
    Select-Object DistinguishedName, SID, member, whenChanged
```

`GG-Lab-Operators` é grupo sintético; substitua pelo objeto do escopo. Esses comandos não coletam
todas as permissões efetivas. Para ACL, consulte o objeto/descritor necessário e interprete direitos,
herança e grupos; mantenha SID/DN para evitar confusão por renomeação.

## Reteste de correção autorizada

- Snapshot anterior, alteração exata e responsável registrados.
- Aresta removida/restrita nos DCs relevantes após propagação verificada.
- Serviço legítimo e acesso administrativo de recuperação funcionando.
- Novo estado do grafo reconciliado com leituras; não apenas rerender do export antigo.
- Logs de alteração e evidências preservados; efeitos irreversíveis declarados no plano.
