class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return print(f'Скорость автомобиля {self.name} - {self.speed} км/ч')

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Speed: {self.speed}\n" \
               f"Color: {self.color}\n" \
               f"Is_police: {self.is_police}\n"

    @staticmethod
    def go():
        return print('Машина начала ехать')

    @staticmethod
    def stop():
        return print('Машина остановилась')

    @staticmethod
    def turn(side):
        return print(f'Машина повернула на {side}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость перевышена!!!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость перевышена!!!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


car = Car(speed=40, color='green', name='BMW')

town_car = TownCar(speed=65, color='green', name='Audi')

police_car = PoliceCar(speed=55, color='black', name='Custom')

print(car)
print(town_car)
print(police_car)

town_car.show_speed()
