# Write your MySQL query statement below

select customer_id,count(*) as count_no_trans
From visits
WHERE visit_id NOT IN (SELECT DISTINCT visit_id FROM Transactions)
GROUP BY customer_id;





