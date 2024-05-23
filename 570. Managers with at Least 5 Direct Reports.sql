# Write your MySQL query statement below
select e1.name
from Employee e1
join Employee e2
on e1.id=e2.managerId
group by e2.managerId
having count(*) >= 5


# Write your MySQL query statement below
select e1.name
from Employee e1
where id in(
    select managerId
    from Employee
    group by managerId
    having count(*) >=5
)
