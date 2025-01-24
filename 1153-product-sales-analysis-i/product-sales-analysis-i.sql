# Write your MySQL query statement below
select Product.product_name,sales.year,sales.price from Sales
  JOIN Product Product 
    ON sales.product_id = Product.product_id 