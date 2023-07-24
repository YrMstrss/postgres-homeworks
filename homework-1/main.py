import psycopg2
import os
import csv


customers_way = os.path.join(os.path.dirname(__file__), 'north_data', 'customers_data.csv')

with psycopg2.connect(host='localhost', database='north', user='postgres', password='qwaszxL1') as conn:
    with conn.cursor() as cur:
        with open(customers_way, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                customer_id, company_name, contact_name = row['customer_id'], row['company_name'], row['contact_name']
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (customer_id, company_name, contact_name))

conn.close()
