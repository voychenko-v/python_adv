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
    CHENG_STATUS_ORDER = sql.SQL('''UPDATE orders SET 
            updated_dt = %s, status = %s WHERE order_id = %s''')
    CHENG_DESCRIPTION_ORDER = sql.SQL('''UPDATE orders SET 
            updated_dt = %s, description = %s WHERE order_id = %s''')

    def __init__(self, order_type, description, status, serial_no, creator_id, order_id=None):
        Order.data_time = str(datetime.now().strftime("%d-%m-%Y"))
        self.created_dt = Order.data_time
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
        super().change_param(self.__class__.CHENG_STATUS_ORDER, new_status, self.order_id)

    def change_description(self, new_description):
        super().change_param(self.__class__.CHENG_DESCRIPTION_ORDER, new_description, self.order_id)

    @classmethod
    def get_id(cls):
        return Order.__id_counter


class Employees(RequestsBd):
    INSERT_EMPLOYEES = sql.SQL('''INSERT INTO employees (fio, position, department_id) 
            VALUES (%s, %s, %s) RETURNING employee_id''')
    CHENG_POSITION_EMPLOYEES = sql.SQL('''UPDATE employees SET status = %s WHERE position = %s''')

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
            cursor.execute(self.__class__.CHENG_POSITION_EMPLOYEES, (new_position, ))


class Departments(RequestsBd):
    INSERT_DEPARTMENT = sql.SQL('''INSERT INTO departments (department_name) VALUES (%s) RETURNING order_department''')
    CHENG_DEPARTMENT_NAME = sql.SQL('''UPDATE departments SET department_name = %s WHERE department_id = %s''')

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
            cursor.execute(self.__class__.CHENG_DEPARTMENT_NAME, (new_department_name, ))


order_1 = Order('Ремонт', 'Ремонт телефона', 'Новая', 3234, 3)
order_1.insert_db()
order_1.change_status('Активная')

