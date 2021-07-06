from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

DB_URL = 'postgresql://postgres:postgresdb@localhost:5432/order_service_db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Department(db.Model):
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(25))


class Employee(db.Model):
    employees_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fio = db.Column(db.String(100))
    position = db.Column(db.String(25))
    department_id = db.Column(db.Integer, db.ForeignKey('department.department_id'), nullable=False)


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_dt = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_dt = db.Column(db.DateTime, nullable=True)
    order_type = db.Column(db.String(20))
    description = db.Column(db.String(100))
    status = db.Column(db.String(15))
    serial_no = db.Column(db.Integer)
    creator_id = db.Column(db.Integer, db.ForeignKey('employee.employees_id'))


@app.route("/ping")
def ping():
    return f'OK {datetime.now()}'


@app.route('/insert_db', methods=['POST'])
def insert_db():
    if request.method == 'POST':
        data_order = json.loads(request.data)
        order_profile = Order(order_type=data_order['order_type'],
                              description=data_order['description'],
                              status=data_order['status'],
                              serial_no=data_order['serial_no'],
                              creator_id=data_order['creator_id'])
        db.session.add(order_profile)
        db.session.flush()
        db.session.commit()
        return 'Create'


@app.route('/insert_employee', methods=['POST'])
def insert_employee():
    if request.method == 'POST':
        data_employee = json.loads(request.data)
        employee_profile = Employee(fio=data_employee['fio'],
                                    position=data_employee['position'],
                                    department_id=data_employee['department_id'])
        db.session.add(employee_profile)
        db.session.flush()
        db.session.commit()
        return 'Create'


@app.route('/insert_department', methods=['POST'])
def insert_department():
    if request.method == 'POST':
        data_department = json.loads(request.data)
        department_profile = Department(department_name=data_department['department_name'])
        db.session.add(department_profile)
        db.session.flush()
        db.session.commit()
        return 'Create'


@app.route('/change_status', methods=['PATCH'])
def change_status():
    if request.method == 'PATCH':
        data_status = json.loads(request.data)
        order_profile = Order(order_id=data_status['order_id'],
                              description=data_status['description'])
        db.session.add(order_profile)
        db.session.flush()
        db.session.commit()
        return f'Change_status {json.loads(request.data)}'


# @app.route('/delete_order/<string:delete_id>', methods=['DELETE'])
# def delete_order(delete_id):
#     with conn, conn.cursor() as cursor:
#         cursor.execute(Order.DELETE_ORDERS_ID, (delete_id, ))
#     return f'Ok - delete_id: {delete_id}'
#
#
# @app.route('/search_order_id/<string:search_id>', methods=['GET'])
# def search_order_id(search_id):
#     with conn, conn.cursor() as cursor:
#         cursor.execute(Order.SEARCH_ORDER_ID, (search_id, ))
#         res = cursor.fetchall()
#     return f'{res}'


app.run(debug=True)