 Análise de Vendas — Northwind Database

Projeto de análise exploratória usando o banco de dados clássico Northwind,
respondendo perguntas de negócio em SQL e replicando a lógica em Python/pandas.

Ferramentas
- PostgreSQL + pgAdmin (consultas SQL)
- Python + pandas + SQLAlchemy (ponte com o banco e replicação das análises)

Conceitos praticados
- SQL: SELECT, WHERE, JOIN, GROUP BY, HAVING, ORDER BY
- pandas: merge, groupby, sort_values, reset_index


Perguntas respondidas
1. Quais são os 5 produtos mais vendidos (em quantidade)?
Camembert Pierrot lidera com 1577 unidades vendidas.

2. Quais clientes fizeram mais de 5 pedidos?
63 clientes atendem esse critério, com destaque para BERGS (18 pedidos).

3. Qual o faturamento total por categoria de produto?
Beverages lidera com US$ 286,526.95, seguida por Dairy Products.

4. Qual funcionário vendeu mais no total?
Margaret Peacock lidera com US$ 250,187.45 em vendas.

5. Qual o ticket médio por país do cliente?
Áustria tem o maior ticket médio (US$ 3,487.42, com 40 pedidos — amostra
consistente), seguida por Ireland.

Estrutura
- `queries.sql` — as 5 queries SQL usadas na análise
- `teste_northwind.py` — mesmas análises replicadas em pandas, conectando ao banco via SQLAlchemy 