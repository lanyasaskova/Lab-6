class Car:

    def __init__(self):
        self.tank = 100
        self.fuel_consumption = 12 #на 100 км
        self.speed = 60

    def max_distance(self):    #метод  1
        self.dist = self.tank / self.fuel_consumption * 100

    def __add__(self, speed):    #доп задание
        new_speed = self.speed + speed
        return new_speed

class Truck(Car):

    def __init__(self, cargo):
        super().__init__()
        self.tank = 500
        self.fuel_consumption = 30 #на 100 км
        self.cargo = cargo #в тоннах
        if self.cargo > 25:
            self.fuel_consumption = 40

    def ratio_truck(self):    #метод 2
        self.truck_ratio = self.cargo / (self.fuel_consumption / 100 * 250)


class Bus(Car):

    def __init__(self, passengers):
        super().__init__()
        self.tank = 250
        self.fuel_consumption = 18 #на 100 км
        self.passengers = passengers
        if passengers > 60:
            self.tank = 300

    def ratio_bus(self):    #метод 2
        self.bus_ratio = self.passengers / (self.fuel_consumption / 100 * 250)

#проверка доп задания:
car1 = Car()
print(car1.speed)
print(car1 + 10) 
