import psycopg2
from psycopg2 import sql
from datetime import datetime

conn = psycopg2.connect('postgres://postgres:postgresdb@localhost:5432/order_service_db')
cursor = conn.cursor()

class Queries:

    __conn = psycopg2.connect('postgres://postgres:postgresdb@localhost:5432/order_service_db')
    __cursor = __conn.cursor()

    def insert_data(self, sql_string):
        sql_string = sql.SQL(sql_string)
        return Queries.__cursor.execute(sql_string)


class Order(Queries):

    __id_counter = 1
    INSERT_ORDERS = sql.SQL('''
            INSERT INTO orders (created_dt, order_type, description, status, serial_no, creator_id) 
            VALUES (%s, %s, %s, %s, %s, %s)
            ''')

    def __init__(self, order_type, description, status, serial_no, creator_id):
        Order.data_time = str(datetime.now().strftime("%d-%m-%Y"))
        self.created_dt = Order.data_time
        self.order_type = order_type
        self.description = description
        self.status = status
        self.serial_no = serial_no
        self.creator_id = creator_id
        self.id = Order.__id_counter
        Order.__id_counter += 1

    def __str__(self):
        return f'Created_dt: {self.created_dt}\n' \
               f'Order_type: {self.order_type}\n' \
               f'Description: {self.description}\n' \
               f'Status: {self.status}\n' \
               f'Serial_no: {self.serial_no}\n' \
               f'Creator_id: {self.creator_id}\n'

    def new_order(self):
        with conn, cursor:
            cursor.execute(self.__class__.INSERT_ORDERS, (datetime.now(), self.order_type, self.description,
                                                          self.status, self.serial_no, self.creator_id))

    def change_status(self):
        pass

    def change_description(self):
        pass

    def change_creator(self):
        pass

    def get_id(self):
        return Order.__id_counter


order_3 = Order('Ремонт', 'Телефона', 'Новая', 2342, 2)
order_3.new_order()
