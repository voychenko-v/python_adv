import psycopg2
from psycopg2 import sql
from datetime import datetime, timedelta

conn = psycopg2.connect('postgres://postgres:postgresdb@localhost:5432/order_service_db')
cursor = conn.cursor()

creator_orders = sql.SQL('''
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    created_dt DATE NOT NULL,
    updated_dt DATE,
    order_type TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    serial_no INTEGER NOT NULL,
    creator_id INTEGER NOT NULL
    );
''')
creator_departments = sql.SQL('''
CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name TEXT NOT NULL
    );
''')
creator_employees = sql.SQL('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL PRIMARY KEY,
    fio TEXT NOT NULL,
    position TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
    ON UPDATE SET NULL
    ON DELETE CASCADE
    );
''')

with conn:
    cursor.execute(creator_orders)
    cursor.execute(creator_departments)
    cursor.execute(creator_employees)


orders_data = [(datetime.now(), 'Установка', 'Установка холодильника', 'Новая', '342564343', 1324),
               (datetime.now(), 'Демонтаж', 'Демонтаж кондиционера', 'Новая', '456831430', 3212)]
employees_data = []
departments_data = []
#
INSERT_ORDERS = sql.SQL('''
INSERT INTO orders (created_dt, order_type, description, status, serial_no, creator_id) VALUES (%s, %s, %s, %s, %s, %s)
''')
# INSERT_EMPLOYEES = sql.SQL('''INSERT INTO employees (fio, position, department_id) VALUES (%s, %s, %s)''')
# INSERT_DEPARTMENTS = sql.SQL('''INSERT INTO departments (department_name) VALUES (%s)''')
# SELECT_QUERY = '''SELECT * FROM employees'''
#
with conn, cursor:
    for orders in orders_data:
        cursor.execute(INSERT_ORDERS, orders)


