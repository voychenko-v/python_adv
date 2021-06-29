import psycopg2
from psycopg2 import sql
from datetime import datetime

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

orders_data = [(datetime.now(), 'Установка', 'Установка холодильника', 'Новая', '3425443', 2),
               (datetime.now(), 'Демонтаж', 'Демонтаж кондиционера', 'Новая', '45631430', 2),
               (datetime.now(), 'Ремонт', 'Ремонт ноутбука', 'Новая', '84763489', 2),
               (datetime.now(), 'Установка', 'Установка холодильника', 'Новая', '95848694', 3),
               (datetime.now(), 'Демонтаж', 'Демонтаж кондиционера', 'Новая', '24673563', 3),
               (datetime.now(), 'Ремонт', 'Ремонт телефона', 'Новая', '7525673', 3),
               (datetime.now(), 'Демонтаж', 'Демонтаж кондиционера', 'Новая', '2653432', 3),
               (datetime.now(), 'Установка', 'Установка кондиционера', 'Новая', '2557474', 4),
               (datetime.now(), 'Демонтаж', 'Демонтаж кондиционера', 'Новая', '23647234', 4),
               (datetime.now(), 'Ремонт', 'Ремонт ноутбука', 'Новая', '7845356', 4),
               (datetime.now(), 'Демонтаж', 'Демонтаж стиральной машины', 'Новая', '34845636', 4),
               (datetime.now(), 'Установка', 'Установка стиральной машины', 'Новая', '74342567', 4),
               (datetime.now(), 'Ремонт', 'Ремонт ноутбука', 'Новая', '34463455', 4),
               (datetime.now(), 'Установка', 'Установка кондиционера', 'Новая', '78547832', 4),
               (datetime.now(), 'Демонтаж', 'Демонтаж холодильника', 'Новая', '3765685', 4)]
departments_data = [['Отдел продаж'], ['Бухгалтерия'], ['Отдел ремонта'], ['ИТ'], ['Склад']]
employees_data = [('Иванов Андрей', 'Менеджер', 1),
                  ('Шевченко Мария', 'Менеджер', 1),
                  ('Полевая Катерина', 'Менеджер', 1),
                  ('Кармалыга Виктор', 'Бухгалтер', 2),
                  ('Псуйко Анна', 'Заместитель бухгалтера', 2),
                  ('Антонович Дмитрий', 'Мастер', 3),
                  ('Князь Ирина', 'Мастер', 3),
                  ('Короп Филип', 'Мастер', 3),
                  ('Стив Джобс', 'FullStack Developer', 4),
                  ('Сорока Юлия', 'Контент менеджер', 4),
                  ('Довбуш Станислав', 'Водитель', 5),
                  ('Климов Богдан', 'Разноробочий', 5)]

INSERT_ORDERS = sql.SQL('''
INSERT INTO orders (created_dt, order_type, description, status, serial_no, creator_id) VALUES (%s, %s, %s, %s, %s, %s)
''')
INSERT_DEPARTMENTS = sql.SQL('''INSERT INTO departments (department_name) VALUES (%s)''')
INSERT_EMPLOYEES = sql.SQL('''INSERT INTO employees (fio, position, department_id) VALUES (%s, %s, %s)''')
SELECT_QUERY = '''SELECT * FROM employees'''

with conn, cursor:
    for orders in orders_data:
        cursor.execute(INSERT_ORDERS, orders)
    for departments in departments_data:
        cursor.execute(INSERT_DEPARTMENTS, departments)
    for employees in employees_data:
        cursor.execute(INSERT_EMPLOYEES, employees)

with conn, cursor:
    cursor.execute('''SELECT * FROM orders WHERE status = 'Новая' AND created_dt = '2021-05-30' AND creator_id = 2''')
    data_status_new = cursor.fetchall()
    cursor.execute('''
    SELECT fio, position, department_name FROM employees 
    LEFT JOIN departments ON employees.department_id = departments.department_id
    ''')
    data_employees = cursor.fetchall()
    cursor.execute('''SELECT status, created_dt, count(*) FROM orders GROUP BY status, created_dt''')
    data_group = cursor.fetchall()
for tmp in data_status_new, data_employees, data_group:
    for tmp_1 in tmp:
        print(tmp_1)

'''
Вручную немного подредачил в базе по статусам, дате - чтобы можно было фильтровать.
Вот что вывело в консоли по запросам:
(56, datetime.date(2021, 5, 30), None, 'Установка', 'Установка кондиционера', 'Новая', 2557474, 2)
(55, datetime.date(2021, 5, 30), None, 'Демонтаж', 'Демонтаж кондиционера', 'Новая', 2653432, 2)
('Иванов Андрей', 'Менеджер', 'Отдел продаж')
('Шевченко Мария', 'Менеджер', 'Отдел продаж')
('Полевая Катерина', 'Менеджер', 'Отдел продаж')
('Кармалыга Виктор', 'Бухгалтер', 'Бухгалтерия')
('Псуйко Анна', 'Заместитель бухгалтера', 'Бухгалтерия')
('Антонович Дмитрий', 'Мастер', 'Отдел ремонта')
('Князь Ирина', 'Мастер', 'Отдел ремонта')
('Короп Филип', 'Мастер', 'Отдел ремонта')
('Стив Джобс', 'FullStack Developer', 'ИТ')
('Сорока Юлия', 'Контент менеджер', 'ИТ')
('Довбуш Станислав', 'Водитель', 'Склад')
('Климов Богдан', 'Разноробочий', 'Склад')
('Активная', datetime.date(2021, 5, 31), 2)
('Закрытая', datetime.date(2021, 5, 31), 2)
('Новая', datetime.date(2021, 5, 30), 3)
('Новая', datetime.date(2021, 5, 31), 5)
('Закрытая', datetime.date(2021, 5, 29), 1)
('Активная', datetime.date(2021, 5, 29), 1)
('Новая', datetime.date(2021, 5, 29), 1)
'''
