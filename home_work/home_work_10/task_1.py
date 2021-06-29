import json
from flask import Flask, request
import psycopg2
from psycopg2 import sql
from datetime import datetime
from abc import ABC, abstractmethod

conn = psycopg2.connect('postgres://postgres:postgresdb@localhost:5432/order_service_db')


class RequestsBd(ABC):
    @abstractmethod
    def insert_db(self, *args, **kwargs):
        pass

    # Реализовол метод для изменения данных в таблицах. Подойтот пока только для Ордерс так как есть поле даты
    def change_param(self, string, param, self_id):
        with conn, conn.cursor() as cursor:
            cursor.execute(string, (datetime.now(), param, self_id))


class Order(RequestsBd):
    __id_counter = 1
    INSERT_ORDERS = sql.SQL('''INSERT INTO orders (created_dt, order_type, description, status, serial_no, creator_id) 
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING order_id''')
    CHANGE_STATUS_ORDER = sql.SQL('''UPDATE orders SET 
            updated_dt = %s, status = %s WHERE order_id = %s''')
    CHANGE_DESCRIPTION_ORDER = sql.SQL('''UPDATE orders SET 
            updated_dt = %s, description = %s WHERE order_id = %s''')
    DELETE_ORDERS_ID = sql.SQL('''DELETE FROM orders WHERE order_id = %s''')
    SEARCH_ORDER_ID = sql.SQL('''SELECT order_id, created_dt, order_type, description, 
            status, serial_no, creator_id FROM orders WHERE order_id = %s''')

    def __init__(self, order_type, description, status, serial_no, creator_id, order_id=None):
        self.created_dt = str(datetime.now().strftime("%d-%m-%Y"))
        self.order_id = order_id
        self.order_type = order_type
        self.description = description
        self.status = status
        self.serial_no = serial_no
        self.creator_id = creator_id
        self.id = Order.__id_counter
        Order.__id_counter += 1

    def __str__(self):
        return f'Created_dt: {self.created_dt}\n' \
               f'Order_id: {self.order_id}\n' \
               f'Order_type: {self.order_type}\n' \
               f'Description: {self.description}\n' \
               f'Status: {self.status}\n' \
               f'Serial_no: {self.serial_no}\n' \
               f'Creator_id: {self.creator_id}\n'

    def insert_db(self):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.INSERT_ORDERS, (datetime.now(), self.order_type, self.description,
                                                          self.status, self.serial_no, self.creator_id))
            order_id = cursor.fetchone()[0]
            self.order_id = order_id
        return {'order_id': order_id}

    def change_status(self, new_status):
        super().change_param(self.__class__.CHANGE_STATUS_ORDER, new_status, self.order_id)
        return 'Ok - change_status'

    def change_description(self, new_description):
        super().change_param(self.__class__.CHANGE_DESCRIPTION_ORDER, new_description, self.order_id)
        return f'Ok - change: {new_description}'

    def delete_order(self, delete_id):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.DELETE_ORDERS_ID, (delete_id, ))
        return f'Ok - delete_id: {delete_id}'

    def search_order_id(self, search_id):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.SEARCH_ORDER_ID, (search_id, ))
        return f'{cursor}'

    @classmethod
    def get_id(cls):
        return Order.__id_counter


class Employees(RequestsBd):
    INSERT_EMPLOYEES = sql.SQL('''INSERT INTO employees (fio, position, department_id) 
            VALUES (%s, %s, %s) RETURNING employee_id''')
    CHANGE_POSITION_EMPLOYEES = sql.SQL('''UPDATE employees SET status = %s WHERE position = %s''')

    def __init__(self, fio, position, department_id, employee_id=None):
        self.fio = fio
        self.position = position
        self.department_id = department_id
        self.employee_id = employee_id

    def insert_db(self):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.INSERT_EMPLOYEES, (self.fio, self.position, self.department_id))
            employee_id = cursor.fetchone()[0]
            self.employee_id = employee_id
        return {'employee_id': employee_id}

    def change_position(self, new_position):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.CHANGE_POSITION_EMPLOYEES, (new_position, ))


class Departments(RequestsBd):
    INSERT_DEPARTMENT = sql.SQL('''INSERT INTO departments (department_name) VALUES (%s) RETURNING order_department''')
    CHANGE_DEPARTMENT_NAME = sql.SQL('''UPDATE departments SET department_name = %s WHERE department_id = %s''')

    def __init__(self, department_name, department_id=None):
        self.department_name = department_name
        self.department_id = department_id

    def insert_db(self):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.INSERT_DEPARTMENT, (self.department_name, ))
            department_id = cursor.fetchone()[0]
            self.department_id = department_id
        return {'department_id': department_id}

    def change_department_name(self, new_department_name):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.CHANGE_DEPARTMENT_NAME, (new_department_name, ))


my_aap = Flask('home_work')


@my_aap.route("/ping")
def ping():
    return f'OK {datetime.now()}'


@my_aap.route('/insert_db', methods=['POST'])
def insert_db():
    if request.method == 'POST':
        data_order = json.loads(request.data)
        order_type = data_order['order_type']
        description = data_order['description']
        status = data_order['status']
        serial_no = data_order['serial_no']
        creator_id = data_order['creator_id']
        with conn, conn.cursor() as cursor:
            cursor.execute(Order.INSERT_ORDERS, (datetime.now(), order_type, description,
                                                 status, serial_no, creator_id))
        return f'Create: {json.loads(request.data)}'


@my_aap.route('/change_status', methods=['PATCH'])
def change_status():
    if request.method == 'PATCH':
        data_status = json.loads(request.data)
        order_id = data_status['order_id']
        new_status = data_status['new_status']
        with conn, conn.cursor() as cursor:
            cursor.execute(Order.CHANGE_STATUS_ORDER, (datetime.now(), new_status, order_id))
        return f'Change_status {json.loads(request.data)}'


@my_aap.route('/delete_order/<string:delete_id>', methods=['DELETE'])
def delete_order(delete_id):
    with conn, conn.cursor() as cursor:
        cursor.execute(Order.DELETE_ORDERS_ID, (delete_id, ))
    return f'Ok - delete_id: {delete_id}'


@my_aap.route('/search_order_id/<string:search_id>', methods=['GET'])
def search_order_id(search_id):
    with conn, conn.cursor() as cursor:
        cursor.execute(Order.SEARCH_ORDER_ID, (search_id, ))
        res = cursor.fetchall()
    return f'{res}'


my_aap.run(debug=True)
