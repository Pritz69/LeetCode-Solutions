# Write your MySQL query statement below
select *
from cinema
where description not in ('boring')
and MOD(id,2)=1
order by rating desc
