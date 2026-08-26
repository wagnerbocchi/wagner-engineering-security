# Arquitetura FastAPI

```text
app/
  main.py
  api/
  domain/
  services/
  repositories/
  integrations/
  models/
  settings.py
```

Não crie camadas vazias por cerimônia. Para CRUD simples, mantenha estrutura menor.

## Lifespan
Abra/feche pools e clients no lifespan da aplicação. Não recrie client HTTP/banco por request sem motivo.

## Readiness
Readiness deve refletir dependências realmente necessárias para servir tráfego. Evite tornar o serviço
indisponível por dependência opcional.
