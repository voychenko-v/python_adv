import json
from flask import Flask, request
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect('postgres://postgres:postgresdb@localhost:5432/order_service_db')


class Employees:
    SEARCH_EMPLOYEES_ID = sql.SQL('''SELECT fio, position FROM employees WHERE employee_id = %s''')

    def __init__(self, fio, position, department_id, employee_id=None):
        self.fio = fio
        self.position = position
        self.department_id = department_id
        self.employee_id = employee_id

    def __str__(self):
        return f'fio: {self.fio}\n' \
               f'position: {self.position}\n' \
               f'department_id: {self.department_id}\n' \


    def search_employee_id(self, search_id):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.SEARCH_EMPLOYEES_ID, (search_id, ))
        return f'{cursor}'


app = Flask('home_work_12')


@app.route('/get_info', methods=['GET'])
def get_info():
    list_data = {}
    if request.method == 'GET':
        data_id = json.loads(request.data)
        print(data_id)
        with conn, conn.cursor() as cursor:
            for key in data_id:
                cursor.execute(Employees.SEARCH_EMPLOYEES_ID, (data_id[key],))
                res = cursor.fetchall()
                list_data[data_id[key]] = list(res[0])
            return json.dumps(list_data)


app.run(debug=True)



# data_id = {"1": 5, "2": 7, "3": 10}
#
# with conn, conn.cursor() as cursor:
#     list_data = {}
#     for key in data_id:
#         cursor.execute(Employees.SEARCH_EMPLOYEES_ID, (data_id[key], ))
#         res = cursor.fetchall()
#         list_data[data_id[key]] = list(res[0])
#     print(list_data)
#     json.dumps(list_data)
#     print(list_data)