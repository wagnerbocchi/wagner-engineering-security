---
name: startup-evaluation
description: >
  Use quando a tarefa for avaliar hipótese de negócio, pitch, customer discovery, piloto, adoção ou viabilidade de startup/projeto. Para arquitetura técnica ou implementação do produto use software-engineering ou siem-soar-development.
---

# Startup / Project Evaluation

Responda em PT-BR técnico, com evidência, exemplos aplicáveis e trade-offs quando relevantes.

## Entradas
Pitch/canvas/entrevistas, público-alvo, problema, solução proposta, evidências, modelo de negócio/adoção e contexto do programa.

## Workflow
1. Avalie clareza do cliente e problema.
2. Diferencie afirmação de evidência.
3. Avalie comportamento de adoção e economia: WTP quando comercial; budget owner, custo evitado, willingness to adopt
   ou impacto equivalente quando WTP não for a métrica correta.
4. Identifique hipóteses críticas não testadas.
5. Produza 3-5 próximos experimentos de maior informação por esforço.

## Scoring
Use `claro / parcial / não claro` por dimensão com justificativa. Não premie complexidade tecnológica nem tamanho de mercado
quando falta evidência do problema.

## Saída
Pontos fortes, lacunas, riscos, próximos experimentos e parecer: avançar / iterar / repensar hipótese.

## Contexto de produto de segurança
- Se a avaliação for da Bocchi Company/Sigmaward, diferencie usuário analista, operador, comprador e responsável pelo risco; não presuma que certificação ou capacidade técnica valida demanda.
- Compare custo de integração, cobertura/qualidade dos dados, confiança para automatizar resposta, isolamento, tempo até valor e custo operacional. EPS sozinho não demonstra benefício de negócio.
- Explicite hipótese de piloto: baseline, fluxo alvo, métrica observável, critério de sucesso, responsável e decisão posterior. Não invente clientes, receita ou métricas de tração.
- Compare construir/comprar e alternativas de adoção quando forem parte da pergunta; apresente trade-offs antes do parecer.
- Consulte fontes atuais quando citar mercado, concorrência ou preços, registrando data e separando dado observado de estimativa.

## Recursos

- Para organizar evidências de problema, adoção e experimentos: [framework](references/framework.md).
