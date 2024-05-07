SELECT customer_id, COUNT(visit_id) as count_no_trans 
FROM Visits
WHERE visit_id NOT IN (
	SELECT visit_id FROM Transactions
	)
GROUP BY customer_id


# Write your MySQL query statement below
SELECT Visits.customer_id , COUNT(Visits.visit_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions on Visits.visit_id=Transactions.visit_id
WHERE Transactions.transaction_id is NULL
GROUP BY Visits.customer_id
