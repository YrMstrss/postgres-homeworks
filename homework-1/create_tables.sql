-- SQL-команды для создания таблиц
CREATE TABLE  customers (
    customer_id  int PRIMARY KEY,
    company_name varchar(100),
    contact_name varchar(100)
)

CREATE TABLE employees (
    employee_id int PRIMARY KEY,
    first_name varchar(100),
    last_name varchar(100),
    title varchar(100),
    birth_date varchar(100),
    notes text
)

CREATE TABLE orders (
    order_id int PRIMARY KEY,
    customer_id int REFERENCES customers (customer_id) NOT NULL,
    employee_id int REFERENCES employees (employee_id) NOT NULL,
    order_date varchar(100),
    ship_city varchar(100)
)