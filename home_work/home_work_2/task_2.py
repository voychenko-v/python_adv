import datetime


class Application:

    __id_counter = 1

    def __init__(self, user_name, id_equipment, status_app):
        Application.data_time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
        self.user_name = user_name
        self.id_equipment = id_equipment
        self.status_app = status_app
        self.id = Application.__id_counter
        self.time = datetime.datetime.now()
        Application.__id_counter += 1

    def __str__(self):
        return f'ID_APP: {self.id}\n' \
               f'Time: {self.time}\n' \
               f'User: {self.user_name}\n' \
               f'ID_EQ: {self.id_equipment}\n' \
               f'Status: {self.status_app}\n'

    def time_active(self):
        if self.status_app == 'Active':
            time_active = datetime.datetime.now() - self.status_app
            return time_active
        else:
            return 'Заявка не в работе'

    def chois_status(self, status):
        self.status_app = status
        return self.status_app

    def get_id(self):
        return Application.__id_counter


app_1 = Application('Max', 'id0456', 'active')
app_2 = Application('Andrey', 'id02332', 'active')
app_3 = Application('Stanislav', 'id03456', 'active')

app_3.chois_status('delete')
print(app_3.status_app)

print(app_1)
print(app_2)
print(app_3)
