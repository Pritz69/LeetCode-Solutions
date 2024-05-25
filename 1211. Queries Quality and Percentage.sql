# Write your MySQL query statement below
select q1.query_name, 
round(avg(q1.rating/q1.position),2) as quality,
round( ( sum(case 
            when q1.rating < 3 then 1
            else 0
            end) * 100 / count(q1.query_name) ),2 ) as poor_query_percentage
from Queries q1
where query_name is not null
group by query_name
