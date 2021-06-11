import datetime

import mongoengine as me
from datetime import datetime

me.connect('HOME_WORK_9')


class Departments(me.Document):
    department_id = me.IntField(required=True)
    department_name = me.StringField(required=True, min_length=4)

    def __str__(self):
        return f'ID: {self.pk} |Department_id: {self.department_id} | Department_name: {self.department_name}'


class Employees(me.Document):
    employees_id = me.IntField(required=True)
    fio = me.StringField(required=True)
    position = me.StringField(required=True)
    # departments = me.ReferenceField(Departments, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return f'ID: {self.pk} |Employees_id: {self.employees_id} |Fio: {self.fio} |Position: {self.position}'


class Orders(me.Document):
    created_dt = me.DateTimeField(required=True)
    updated_dt = me.DateTimeField()
    order_type = me.StringField(required=True, min_length=4)
    description = me.StringField(required=True, min_length=4)
    status = me.StringField(required=True)
    serial_no = me.IntField(required=True, min_length=4, max_value=99999)
    creator_id = me.IntField(required=True)
    # creator_id = me.ReferenceField(Employees, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return f'ID: {self.pk}  |'\
               f'Created_dt: {self.created_dt} |'\
               f'Updated_dt: {self.updated_dt} |'\
               f'Order_type: {self.order_type} |'\
               f'Description: {self.description} |'\
               f'Status: {self.status} |'\
               f'Serial_no: {self.serial_no} |'\
               f'Creator_id: {self.creator_id} |'

    def save(self, *args, **kwargs):
        self.created_dt = datetime.now()
        return super().save(*args, **kwargs)

    def new_order(self):
        pass

    def change_status(self, value_orders):
        pass

    def delete_user(self):
        self.__class__.objects.all().delete()
        return print('ok')

data_orders = Orders(created_dt=datetime.now(), order_type='Ремонт', description='Ремонт ноутбука',
                     status='Новая', serial_no='2234', creator_id='3')

# Orders.objects.all().delete()

# data_orders.save()
Orders.delete()
