# Metodologia AI Red Team

## Threat surfaces
- prompt direto e indireto;
- RAG/index/document ingestion;
- tool/function calling;
- memória e contexto persistente;
- MCP/servidores e descrições de ferramentas;
- output rendering e downstream parsers;
- model/provider API e quotas;
- fine-tuning/training data e supply chain.

## Evidência mínima
Para cada caso: test_id, precondition, system version/model, exact input, retrieved context quando houver,
output, tool calls, side effects, expected behavior, actual behavior e repetibilidade em N execuções.

## Agentic systems
Teste least privilege de tools, confirmação para ações críticas, isolamento entre tenants, poisoning de
memória/contexto, tool confusion, credential exposure e capacidade de encadear ações inesperadas.
