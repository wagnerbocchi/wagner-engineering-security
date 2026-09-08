# Troubleshooting por camada

## DNS
```bash
dig +short example.com
dig @1.1.1.1 example.com
resolvectl status
```
Compare resolver local, autoritativo e cache.

## TCP/TLS/HTTP
```bash
nc -vz host 443
openssl s_client -connect host:443 -servername host -verify_hostname host -verify_return_error </dev/null
curl -v --connect-timeout 5 --max-time 15 https://host/health
```

## Socket/processo
```bash
ss -lntup
systemctl status <service>
journalctl -u <service> --since '-15 min'
```

## Pacotes
```bash
tcpdump -ni any host <ip> and port <port>
tshark -i any -f 'host <ip> and port <port>'
```
Use captura para distinguir "não saiu", "saiu sem resposta", reset, retransmissão ou problema TLS/aplicação.

Substitua `host` pelo destino autorizado; use a CA apropriada quando privada. Não trate sucesso com
validação TLS desabilitada como prova de configuração correta. `curl -v` pode exibir headers sensíveis:
sanitize antes de anexar evidência. Limite tempo e volume de capturas no ambiente real.
