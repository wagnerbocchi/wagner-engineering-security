---
name: networks-servers
description: >
  Use quando o problema principal estiver em rede ou SO: DNS, rota, TCP/UDP, TLS, proxy, firewall, SSH ou serviço Linux/Windows. Para runtime de containers use docker-containers; para segurança do domínio use active-directory-security.
---

# Networks & Servers

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

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

## Hipóteses e validação discriminante
- Registre origem/destino, namespace, IPv4/IPv6, resolução e proxy usados pelo processo que falha; sucesso no host não prova sucesso dentro do container.
- Ordene hipóteses por probabilidade e custo, associando teste, resultado esperado e interpretação. Separe timeout, recusa, reset, erro TLS e erro de autorização HTTP.
- Verifique SNI, cadeia, hostname e relógio. Bypass de validação TLS serve apenas a comparação explícita e não constitui correção nem teste de sucesso.
- Em captura, restrinja interface, host, porta e duração; preserve PCAP e remova dados sensíveis ao compartilhar evidência.
- Após mudança crítica, teste uma nova sessão pela origem real, resolução, TLS, serviço e acesso de recuperação; registre gatilho e comando de rollback.

## Recursos

- Para testes por camada: [troubleshooting](references/troubleshooting.md).
- Para redução de superfície e mudança remota: [hardening](references/hardening.md).
