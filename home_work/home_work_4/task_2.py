from abc import ABC, abstractmethod


class OfficeEquipment(ABC):

    @abstractmethod
    def power(self, off=True):
        return f'Power {off}'

    @abstractmethod
    def start(self):
        return 'Start'

    @abstractmethod
    def stop(self):
        return 'Stop'


class EquipmentData:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f'{self.__class__} Mодель: {self.model} | Цена: {self.price}'


class Printer(OfficeEquipment, EquipmentData):
    """Чернила"""
    ink = 100

    def power(self, off=True):
        if off is True:
            return f'Принтер - {self.model} выключен.'
        return f'Принтер - {self.model} включен.'

    def start(self):
        return 'Старт'

    def stop(self):
        return 'Стоп'

    def check_ink(self):
        if self.ink <= 10:
            return f'Нужно заправить чернила осталось - {self.ink} %'
        return f'Чернил осталось - {self.ink}%'


class Scanner(OfficeEquipment, EquipmentData):

    def power(self, off=True):
        if off is True:
            return f'Сканер - {self.model} выключен.'
        return f'Сканер - {self.model} включен.'

    def start(self):
        return 'Старт'

    def stop(self):
        return 'Стоп'


class Xerox(OfficeEquipment, EquipmentData):

    def power(self, off=True):
        if off is True:
            return f'Ксерокс - {self.model} выключен.'
        return f'Ксерокс - {self.model} включен.'

    def start(self):
        return 'Старт'

    def stop(self):
        return 'Стоп'

    def copies_num(self, num):
        return f'Печатать {num} копий документа'


printer_tmp = Printer('PR3434', 1200)
scanner_tmp = Scanner('SK4534', 3400)
xerox_tmp = Xerox('XE4534', 3400)
print(printer_tmp)
print(printer_tmp.check_ink())


class Warehouse:

    list_equipment = []

    def append_warehouse(self, data):
        self.list_equipment.append(data)
        return f'Добавлено: {data}'

    def __iter__(self):
        count = 1
        for list_item in self.list_equipment:
            yield f'{count}: {list_item}'
            count += 1


list_data = Warehouse()
print(list_data)
list_data.append_warehouse(printer_tmp)
list_data.append_warehouse(scanner_tmp)
list_data.append_warehouse(xerox_tmp)

print(list_data.list_equipment)

for list_eq in list_data:
    print(list_eq)
