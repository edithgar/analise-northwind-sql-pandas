SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';

SELECT p.product_name, SUM(od.quantity) AS total_sell
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sell DESC
LIMIT 5;

SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 5;

SELECT c.category_name, SUM(od.quantity * od.unit_price) AS faturamento
FROM order_details od
JOIN products p ON od.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY faturamento DESC;

SELECT e.employee_id, e.first_name, e.last_name, SUM(od.quantity * od.unit_price) AS total_vendido
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN order_details od ON o.order_id = od.order_id
GROUP BY e.employee_id, e.first_name, e.last_name
ORDER BY total_vendido DESC;

SELECT c.country,
       SUM(od.quantity * od.unit_price) / COUNT(DISTINCT o.order_id) AS ticket_medio,
       COUNT(DISTINCT o.order_id) AS total_pedidos
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
GROUP BY c.country
ORDER BY ticket_medio DESC;