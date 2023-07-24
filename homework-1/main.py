import psycopg2
import os
import csv


customers_way = os.path.join(os.path.dirname(__file__), 'north_data', 'customers_data.csv')

with open(customers_way, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        customer_id, company_name, contact_name = row['customer_id'], row['company_name'], row['contact_name']
        print(customer_id, company_name, contact_name)

