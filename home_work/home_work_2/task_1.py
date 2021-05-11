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
        return print(self)

    def go(self):
        return print('Машина начала ехать')

    def stop(self):
        return print('Машина остановилась')

    def turn(self, side):
        return print(f'Машина повернула на {side}')


car = Car(speed=40, color='green', name='bmw', is_police=True)


