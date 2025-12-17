# select
#        c.country,
#        avg(sub.order_count) as avg_orders_per_customer
# from customers c,
#      (
#        select customer_id, count(*) as order_count
#        from orders
#        group by customer_id
#      ) sub
# where c.customer_id = sub.customer_id
# group by c.country;
#
#
# select
#        c.company_name,
#        count(o.order_id) as orders_count
# from customers c, orders o
# where c.customer_id = o.customer_id
#   and c.country = 'USA'
# group by c.company_name;
#
#
# select
#        c.country,
#        count(o.order_id) as late_orders_count
# from customers c, orders o
# where c.customer_id = o.customer_id
#   and o.shipped_date > o.required_date
# group by c.country;
#
#
# select
#        e.employee_id,
#        extract(year from o.order_date) as year,
#        count(o.order_id) as orders_count
# from employees e, orders o
# where e.employee_id = o.employee_id
#   and e.country = 'USA'
# group by e.employee_id, extract(year from o.order_date)
# order by e.employee_id, year;
#
#
# select
#        extract(year from o.order_date) as year,
#        count(od.order_id) as orders_count
# from orders o, order_details od, products p
# where o.order_id = od.order_id
#   and od.product_id = p.product_id
#   and p.unit_price = (
#         select min(unit_price)
#         from products
#       )
# group by extract(year from o.order_date)
# order by year;
#
#
# select
#        s.company_name,
#        extract(year from o.order_date) as year,
#        count(od.order_id) as orders_count
# from suppliers s, products p, order_details od, orders o
# where s.supplier_id = p.supplier_id
#   and p.product_id = od.product_id
#   and od.order_id = o.order_id
# group by s.company_name, extract(year from o.order_date)
# order by s.company_name, year;