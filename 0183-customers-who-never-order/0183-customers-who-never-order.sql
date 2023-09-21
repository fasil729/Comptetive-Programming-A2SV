# Write your MySQL query statement below
SELECT name as Customers From 
Customers LEFT JOIN Orders ON
Customers.id = Orders.customerId
where Orders.id is null;