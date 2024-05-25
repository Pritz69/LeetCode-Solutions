# Write your MySQL query statement below
select 
    round (
            (
            select count(*) 
            from 
            (
            select customer_id
            from Delivery 
            group by customer_id 
            having min(order_date)=min(customer_pref_delivery_date)
            )as immediate_orders
            )*100.0/count(distinct customer_id) 
        ,2) as immediate_percentage
from Delivery
