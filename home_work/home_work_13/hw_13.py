
from flask import Flask, render_template, url_for
import psycopg2
from psycopg2 import sql
from datetime import datetime

conn = psycopg2.connect('postgres://postgres:postgresdb@localhost:5432/order_service_db')


class Order:

    SHOW_ORDERS = sql.SQL('''SELECT order_id, created_dt, order_type, description, 
            status, serial_no, creator_id FROM orders ''')

    def __init__(self, order_type, description, status, serial_no, creator_id, order_id=None):
        self.created_dt = str(datetime.now().strftime("%d-%m-%Y"))
        self.order_id = order_id
        self.order_type = order_type
        self.description = description
        self.status = status
        self.serial_no = serial_no
        self.creator_id = creator_id


class Employees:
    SHOW_EMPLOYEES = sql.SQL('''SELECT employee_id, fio, position, department_id FROM employees ''')

    def __init__(self, fio, position, department_id, employee_id=None):
        self.fio = fio
        self.position = position
        self.department_id = department_id
        self.employee_id = employee_id


class Departments:
    SHOW_DEPARTMENT = sql.SQL('''SELECT department_id, department_name FROM departments ''')

    def __init__(self, department_name, department_id=None):
        self.department_name = department_name
        self.department_id = department_id


my_aap = Flask('home_work')


@my_aap.route('/')
def index():
    return render_template('index.html')


@my_aap.route('/show_orders')
def show_orders():
    with conn, conn.cursor() as cursor:
        cursor.execute(Order.SHOW_ORDERS, )
        res = cursor.fetchall()
    return render_template('show_orders.html', orders_list=res)


@my_aap.route('/show_emp')
def show_emp():
    with conn, conn.cursor() as cursor:
        cursor.execute(Employees.SHOW_EMPLOYEES, )
        res = cursor.fetchall()
    return render_template('show_emp.html', employees_list=res)


@my_aap.route('/show_dep')
def show_dep():
    with conn, conn.cursor() as cursor:
        cursor.execute(Departments.SHOW_DEPARTMENT, )
        res = cursor.fetchall()
    return render_template('show_dep.html', department_list=res)


@my_aap.route('/onas')
def onas():
    return render_template('onas.html')


my_aap.run(debug=True)
