# Automação robusta

## Cliente HTTP
```python
import httpx

class APIClient:
    def __init__(self, base_url: str, token: str) -> None:
        self.client = httpx.Client(
            base_url=base_url,
            headers={"Authorization": f"Bearer {token}"},
            timeout=httpx.Timeout(10.0),
        )

    def close(self) -> None:
        self.client.close()

    def get_event(self, event_id: str) -> dict:
        # Restrict this example to a single URL path segment.
        if not event_id or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in event_id):
            raise ValueError("event_id deve ser um identificador simples")
        r = self.client.get(f"/events/{event_id}")
        r.raise_for_status()
        return r.json()
```

Feche o client em `finally` ou adapte a classe para context manager. Reutilize um client por ciclo de
vida apropriado, em vez de criar conexões sem fechamento por request. O exemplo não implementa retry,
paginação ou validação do schema de resposta; adicione conforme o contrato real.

## Idempotência
Para ações remotas, derive uma chave estável do evento/origem e persista o resultado. Reexecução deve
ser segura e retornar o recurso existente quando possível.

## Retry
Retry somente em falhas transitórias (timeouts, 429, alguns 5xx). Não faça retry cego em 4xx funcionais
ou operações não idempotentes sem chave de idempotência.
