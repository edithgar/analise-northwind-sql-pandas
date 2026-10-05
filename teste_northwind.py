import pandas as pd 
from getpass import getpass
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

senha = getpass("Senha do postgres: ")

url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password=senha,
    host="localhost",
    port=5432,
    database="northwind",
    )
engine = create_engine(url)

query = """
SELECT p.product_name, SUM(od.quantity) AS total_sell
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sell DESC
LIMIT 5;
"""

try:
    df = pd.read_sql(query, engine)
    print(df)
except UnicodeDecodeError as e:
    print(e.object.decode("cp1252"))

# Puxa as tabelas inteiras para o pandas
order_details = pd.read_sql("SELECT * FROM order_details", engine)
products = pd.read_sql("SELECT * FROM products", engine)

# Faz o JOIN no pandas (equivale ao JOIN do SQL)
juntas = order_details.merge(products, on="product_id")

# Agrupa e soma (equivale ao GROUP BY + SUM)
top5 = (juntas.groupby("product_name")["quantity"]
              .sum()
              .sort_values(ascending=False)
              .head(5))
print(top5)
# Carrega as tabelas que faltam
customers = pd.read_sql("SELECT * FROM customers", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)
employees = pd.read_sql("SELECT * FROM employees", engine)
categories = pd.read_sql("SELECT * FROM categories", engine)

# 2. Clientes com mais de 5 pedidos
pedidos_por_cliente = (orders.groupby("customer_id")["order_id"]
                              .count()
                              .reset_index(name="total_orders"))
clientes_fieis = pedidos_por_cliente[pedidos_por_cliente["total_orders"] > 5]
print(clientes_fieis)

# 3. Faturamento por categoria
juntas2 = order_details.merge(products[["product_id", "category_id"]], on="product_id").merge(categories, on="category_id")
juntas2["faturamento"] = juntas2["quantity"] * juntas2["unit_price"]
faturamento_categoria = (juntas2.groupby("category_name")["faturamento"]
                                  .sum()
                                  .sort_values(ascending=False))
print(faturamento_categoria)

# 4. Vendas por funcionário
juntas3 = orders.merge(order_details, on="order_id").merge(employees, on="employee_id")
juntas3["total_vendido"] = juntas3["quantity"] * juntas3["unit_price"]
vendas_funcionario = (juntas3.groupby(["employee_id", "first_name", "last_name"])["total_vendido"]
                              .sum()
                              .sort_values(ascending=False))
print(vendas_funcionario)

# 5. Ticket médio por país
juntas4 = customers.merge(orders, on="customer_id").merge(order_details, on="order_id")
juntas4["valor"] = juntas4["quantity"] * juntas4["unit_price"]
ticket_pais = (juntas4.groupby("country")
                       .apply(lambda g: g["valor"].sum() / g["order_id"].nunique())
                       .sort_values(ascending=False))
print(ticket_pais)