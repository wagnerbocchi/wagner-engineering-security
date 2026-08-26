# Hardening de servidor

Prioridades:
1. patching e inventário;
2. autenticação forte e menor privilégio;
3. superfície de rede mínima;
4. logging/auditoria;
5. backups testados;
6. baseline de configuração e detecção de drift.

Para SSH: chaves/SSO conforme ambiente, desabilitar autenticação insegura quando possível, limitar origem,
controlar sudo e manter acesso de recuperação. Sempre valide `sshd -t` antes de reload.

Para firewall: mantenha política documentada e rollback. Nunca aplique mudança remota destrutiva sem caminho de recuperação.
