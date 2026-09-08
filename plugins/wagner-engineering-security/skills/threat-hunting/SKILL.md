---
name: threat-hunting
description: >
  Use quando a tarefa for conduzir hunting proativo orientado por hipótese, investigar comportamento
  adversário sem incidente confirmado ou avaliar lacunas de telemetria e evidência negativa.
  Para incidente em curso use incident-response; para transformar hipótese em regra use detection-engineering.
---

# Threat hunting orientado por hipótese

Entregue em PT-BR técnico uma conclusão limitada ao que os dados permitem. Adote o schema e mecanismo
de consulta existentes; não invente sintaxe de query do Sigmaward nem presuma integração já implementada.

## Fluxo investigativo

1. Formule hipótese falsificável: comportamento, população de ativos/identidades, janela e evidência
   que a sustentaria ou enfraqueceria. Diferencie IOC conhecido de hipótese comportamental.
2. Inspecione amostras e saúde da coleta antes da query: fonte, campos, retenção, atrasos, gaps,
   timezone/clock skew e cardinalidade. Preserve timestamp original e origem do offset aplicado.
3. Construa consulta inicial com parâmetros explícitos de tenant e janela. Valide contra um controle
   conhecido; zero resultado com controle ausente torna o teste inconclusivo.
4. Faça pivôs por evidência: identidade, host, processo pai/filho, sessão, IP e recurso cloud.
   Correlacione por identificadores estáveis; IP reutilizado/NAT ou PID isolado não prova mesma entidade.
5. Compare explicações benignas e adversárias, registrando cada consulta, recorte e resultado.
   Se houver comprometimento plausível em curso, encaminhe evidência ao fluxo de IR.
6. Encerre como sustentada, não sustentada no recorte observado ou inconclusiva; registre cobertura
   efetiva e limitações. Proponha reparo de telemetria ou uma detecção testável quando sustentado pelos dados.

## Evidência negativa

Zero hits não comprova ausência de comprometimento. Se faltam 6h de um sensor numa janela de 24h,
registre a lacuna desse sensor; não atribua automaticamente 75% de cobertura à investigação inteira.
Fonte alternativa só cobre o comportamento que realmente observa. Timestamp sem offset continua
ambíguo até existir evidência que permita normalização, inclusive em transições de horário de verão.

## Entrega reproduzível

Use [registro de hunt](references/hunt-record.md) para hipótese, query, proveniência, lacunas e conclusão.
Liste próximos passos por ganho de informação e custo. Mapeie ATT&CK apenas após validar a técnica na
fonte oficial quando necessário; a tag não comprova cobertura operacional.
