# Dockerfile e runtime

## Dockerfile
- multi-stage builds;
- copie lockfiles antes do source para aproveitar cache;
- use base mínima compatível, não necessariamente a menor possível;
- `HEALTHCHECK` só quando o runtime realmente usa esse sinal;
- entrypoint deve encaminhar sinais corretamente.

## Troubleshooting
```bash
docker inspect <container>
docker logs --tail=200 <container>
docker exec -it <container> sh
docker image inspect <image>
docker history <image>
docker stats
```

Cheque DNS, network namespace, bind mounts, permissões, cgroups/OOM, architecture mismatch e registry auth.
