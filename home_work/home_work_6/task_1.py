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

# orders_data = [(datetime.now(), 'Установка', 'Установка холодильника', 'Новая', '3425443', 1324),
#                (datetime.now(), 'Демонтаж', 'Демонтаж кондиционера', 'Новая', '45631430', 3212),
#                (datetime.now(), 'Ремонт', 'Ремонт ноутбука', 'Новая', '84763489', 4536),
#                (datetime.now(), 'Установка', 'Установка холодильника', 'Новая', '95848694', 7956),
#                (datetime.now(), 'Демонтаж', 'Демонтаж кондиционера', 'Новая', '24673563', 8645),
#                (datetime.now(), 'Ремонт', 'Ремонт телефона', 'Новая', '7525673', 8453),
#                (datetime.now(), 'Демонтаж', 'Демонтаж кондиционера', 'Новая', '2653432', 3658),
#                (datetime.now(), 'Установка', 'Установка кондиционера', 'Новая', '2557474', 9765),
#                (datetime.now(), 'Демонтаж', 'Демонтаж кондиционера', 'Новая', '23647234', 3676),
#                (datetime.now(), 'Ремонт', 'Ремонт ноутбука', 'Новая', '7845356', 5675),
#                (datetime.now(), 'Демонтаж', 'Демонтаж стиральной машины', 'Новая', '34845636', 5980),
#                (datetime.now(), 'Установка', 'Установка стиральной машины', 'Новая', '74342567', 6980),
#                (datetime.now(), 'Ремонт', 'Ремонт ноутбука', 'Новая', '34463455', 7686),
#                (datetime.now(), 'Установка', 'Установка кондиционера', 'Новая', '78547832', 4789),
#                (datetime.now(), 'Демонтаж', 'Демонтаж холодильника', 'Новая', '3765685', 3467)]
# departments_data = [['Отдел продаж'], ['Бухгалтерия'], ['Отдел ремонта'], ['ИТ'], ['Склад']]
# employees_data = [('Иванов Андрей', 'Менеджер', 1),
#                   ('Шевченко Мария', 'Менеджер', 1),
#                   ('Полевая Катерина', 'Менеджер', 1),
#                   ('Кармалыга Виктор', 'Бухгалтер', 2),
#                   ('Псуйко Анна', 'Заместитель бухгалтера', 2),
#                   ('Антонович Дмитрий', 'Мастер', 3),
#                   ('Князь Ирина', 'Мастер', 3),
#                   ('Короп Филип', 'Мастер', 3),
#                   ('Стив Джобс', 'FullStack Developer', 4),
#                   ('Сорока Юлия', 'Контент менеджер', 4),
#                   ('Довбуш Станислав', 'Водитель', 5),
#                   ('Климов Богдан', 'Разноробочий', 5)]
#
# INSERT_ORDERS = sql.SQL('''
# INSERT INTO orders (created_dt, order_type, description, status, serial_no, creator_id) VALUES (%s, %s, %s, %s, %s, %s)
# ''')
# INSERT_DEPARTMENTS = sql.SQL('''INSERT INTO departments (department_name) VALUES (%s)''')
# INSERT_EMPLOYEES = sql.SQL('''INSERT INTO employees (fio, position, department_id) VALUES (%s, %s, %s)''')
# SELECT_QUERY = '''SELECT * FROM employees'''
#
# with conn, cursor:
#     for orders in orders_data:
#         cursor.execute(INSERT_ORDERS, orders)
#     for departments in departments_data:
#         cursor.execute(INSERT_DEPARTMENTS, departments)
#     for employees in employees_data:
#         cursor.execute(INSERT_EMPLOYEES, employees)
