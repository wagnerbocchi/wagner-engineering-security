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
openssl s_client -connect host:443 -servername host </dev/null
curl -vk --connect-timeout 5 https://host/health
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
