---
name: networks-servers
description: >
  Redes, Linux/Windows servers, DNS, TLS, HTTP proxies, firewalls, SSH, análise de tráfego,
  observabilidade e troubleshooting de conectividade. Use quando o problema principal estiver na
  camada de rede/SO. Para containers ou aplicação, prefira skills específicas.
---

# Networks & Servers

## Workflow de troubleshooting
1. Defina origem, destino, protocolo, porta e comportamento esperado.
2. Teste camada por camada: DNS → rota → TCP/UDP → TLS → HTTP/aplicação → autorização.
3. Colete evidência antes de mudar configuração.
4. Ordene hipóteses por probabilidade e custo de teste.
5. Faça uma mudança por vez e registre resultado.

## Ferramentas
`ip`, `ss`, `dig`, `resolvectl`, `curl`, `openssl s_client`, `mtr`, `traceroute`, `tcpdump`,
`tshark`, Wireshark, `nft`, `iptables` quando legado, `journalctl`, `systemctl`, PowerShell.

## Mudanças críticas
Para SSH, firewall, rota, DNS ou proxy em máquina remota:
- confirme console/out-of-band ou segunda sessão;
- valide sintaxe antes do reload;
- abra regra nova antes de fechar a antiga;
- teste nova sessão/conectividade;
- só então remova configuração anterior.

Mudar a porta SSH reduz ruído, mas não substitui autenticação forte, MFA/bastion quando aplicável,
restrição de origem e atualização do sistema.

## Recursos
- `references/troubleshooting.md`
- `references/hardening.md`

## Verificações finais
- Confirme que a resposta atende ao objetivo real, não só às palavras-chave.
- Declare suposições que possam alterar a solução.
- Quando versões, APIs, CVEs, padrões ou comportamento de produto puderem ter mudado, valide em documentação atual antes de afirmar.
- Em mudanças de produção, inclua rollback e validação pós-mudança.
- Prefira exemplos executáveis, comandos completos e critérios objetivos de sucesso.
