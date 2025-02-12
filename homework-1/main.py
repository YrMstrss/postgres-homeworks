import psycopg2
import os
import csv
from datetime import datetime

customers_way = os.path.join(os.path.dirname(__file__), 'north_data', 'customers_data.csv')
employees_way = os.path.join(os.path.dirname(__file__), 'north_data', 'employees_data.csv')
orders_way = os.path.join(os.path.dirname(__file__), 'north_data', 'orders_data.csv')

with psycopg2.connect(host='localhost', database='north', user='postgres', password='qwaszxL1') as conn:
    with conn.cursor() as cur:
        with open(customers_way, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                customer_id, company_name, contact_name = row['customer_id'], row['company_name'], row['contact_name']
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (customer_id, company_name, contact_name))

    with conn.cursor() as cur:
        with open(employees_way, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                employee_id, first_name, last_name, title, birth_date, notes = \
                    row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'], \
                        row['notes']
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                            (int(employee_id), first_name, last_name, title, datetime.strptime(birth_date, '%Y-%m-%d'),
                             notes))

    with conn.cursor() as cur:
        with open(orders_way, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                order_id, customer_id, employee_id, order_date, ship_city = \
                    row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city']
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                            (int(order_id), customer_id, int(employee_id), datetime.strptime(order_date, '%Y-%m-%d'),
                             ship_city))

conn.close()
