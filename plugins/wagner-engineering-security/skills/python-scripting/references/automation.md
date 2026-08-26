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

    def get_event(self, event_id: str) -> dict:
        r = self.client.get(f"/events/{event_id}")
        r.raise_for_status()
        return r.json()
```

## Idempotência
Para ações remotas, derive uma chave estável do evento/origem e persista o resultado. Reexecução deve
ser segura e retornar o recurso existente quando possível.

## Retry
Retry somente em falhas transitórias (timeouts, 429, alguns 5xx). Não faça retry cego em 4xx funcionais
ou operações não idempotentes sem chave de idempotência.
