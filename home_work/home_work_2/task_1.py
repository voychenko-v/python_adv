class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        # self.is_police = is_police

    def show_speed(self):
        return print(f'Скорость {self.speed} км/ч')

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
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} перевышена')
        super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} перевышена')
        super().show_speed()


car = Car(speed=40, color='green', name='bmw')

town_car = TownCar(speed=65, color='green', name='Audi')

print(car)

print(town_car)
town_car.show_speed()



