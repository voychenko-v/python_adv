class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            print('Danger')
        return print(f'Скорость автомобиля {self.speed} км/ч')

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
    pass

class WorKCar(Car):
    pass


car = Car(speed=40, color='green', name='bmw', is_police=False)

print(car)






