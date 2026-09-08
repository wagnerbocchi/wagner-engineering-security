---
name: active-directory-security
description: >
  Use quando a tarefa envolver avaliação de segurança de Active Directory: ACLs, grupos privilegiados,
  trusts, delegação Kerberos, AD CS, contas de serviço ou caminhos BloodHound.
  Para rede/serviço Windows use networks-servers; para IAM cloud use cloud-iam-security.
---

# Segurança de Active Directory

Responda em PT-BR técnico, preservando ROE e autorização já definidos. Identifique domínio/floresta,
identidade de coleta, janela e operações permitidas. Uma avaliação de leitura deve produzir evidência
de configuração sem alterar grupos, ACLs, contas ou executar técnicas de extração de credenciais.

## Avaliação de caminhos

1. Verifique origem, data e cobertura da coleta. Um grafo antigo descreve uma hipótese histórica;
   a coleta não deve ser tratada como retrato atual sem revalidar arestas relevantes.
2. Modele principal → relação/permissão → objeto → precondição → impacto potencial.
   Correlacione grupos aninhados, ACLs/herança, ownership e estado atual dos objetos.
3. Em Kerberos, avalie tipo de delegação, identidades/serviços envolvidos e precondições reais.
   Em AD CS, relacione template, CA, permissões de enrollment, emissão e autenticação resultante;
   flags isoladas não bastam para confirmar um caminho explorável.
4. Priorize arestas que rompem fronteiras de administração, contas de serviço e caminhos a ativos
   críticos. Valide leituras pontuais antes de recomendar coleta ampla ou teste ativo.
5. Separe caminho estrutural, precondições verificadas e exploração demonstrada. Se o ROE não permite
   a prova ativa, entregue a conclusão estática com limites e uma proposta de validação em laboratório.
6. Recomende correção da relação responsável e avalie dependências de serviço, propagação/replicação
   e método de recuperação antes de qualquer mudança autorizada.

## Prova mínima

| Aresta | Registrar |
|---|---|
| Grupo → grupo/conta | SID/DN, associação direta ou transitiva e data da leitura |
| Principal → objeto | ACE/direito efetivo, herança e precondições |
| Delegação → serviço | Tipo, alvos e configuração corroborada |
| Template → identidade | Conjunto de condições de emissão e autorização verificadas |

Use [validação de arestas](references/path-validation.md) para organizar evidência e reteste.
Reporte objetos inacessíveis, coleta incompleta e dados antigos como limitações. Não afirme Domain Admin
obtido apenas porque uma ferramenta desenhou o caminho.

Consulte as [orientações Microsoft](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory)
e a documentação da versão real para hardening e comportamento de autenticação.
