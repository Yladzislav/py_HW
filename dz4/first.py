
class Vehicle:
    def __init__(self, max_speed : float, mileage : float):
        self._max_speed = max_speed
        self.__mileage = mileage

    def display_info(self):
        print(f"Max speed : {self._max_speed}" , f"Mileage : {self.__mileage}", sep = '\n')

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.pas_cap = capacity

    def display_info(self):
        super().display_info()
        print(f"Passanger capacity : {self.pas_cap}")

    # def display_info(self):
    #     print(f"Max speed : {self._max_speed}" , f"Mileage : {self._Vehicle__mileage}", f"Passanger capacity : {self.pas_cap}", sep = '\n')

o = Bus(70, 500, 40)
o.display_info()

'''
1) Создайте базовый класс Vehicle (транспортное средство) с защищённым (_protected) атрибутом max_speed 
и приватным (__private) атрибутом mileage.
 - Добавьте публичный метод display_info(), который выводит эти атрибуты.
 - Создайте дочерний класс Bus, который наследует Vehicle и добавляет атрибут passenger_capacity.
 - Переопределите метод display_info() в Bus, чтобы он показывал также вместимость пассажиров.

bus = Bus(180, 10000, 50)
bus.display_info()  # Должно вывести: Max Speed: 180, Mileage: 10000, Passenger Capacity: 50
'''