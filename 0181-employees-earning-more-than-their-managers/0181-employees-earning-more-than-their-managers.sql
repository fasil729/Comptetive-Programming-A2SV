# Write your MySQL query statement below
SELECT e1.name as Employee FROM
Employee AS e1 JOIN Employee AS e2  on 
e1.managerId = e2.id where
e1.salary > e2.salary;