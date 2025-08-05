
class Temperature:
    def __init__(self, degree : float):
        """
        in celsius
        """
        self.__celsius : float = degree

    def __setattr__(self, name, degree):
        assert degree > -273.15, ValueError

        #print('called set')

        if name == 'celsius':
            name = '_Temperature__celsius'
    
        super().__setattr__(name, degree)


    def __getattribute__(self, name):

        #print('called get')

        print(name)
        if name == 'farenheit':
            return ((self.__celsius * 9) / 5 + 32)
        if name == 'celsius':
            name = '_Temperature__celsius'

        return super().__getattribute__(name)
    
    def __getattr__ (self, name):
        
        #print('called gatattr')

        super().__getattr__(name)
    



temp = Temperature(25)
# print('-'*20)
# print(temp.celsius)
# print('-'*20)
# print(temp.farenheit)
# print('-'*20)
# temp.celsius = -200
# print('-'*20)
# print(temp.celsius)
# print('-'*20)
# print(temp.farenheit)
# print('-'*20)
# print(temp.celsius)
# print('-'*20)
# temp.celsius = 100
# print('-'*20)
# print(temp.celsius)
# print('-'*20)
# print(temp.farenheit)

'''
2) Создайте класс Temperature с приватным атрибутом __celsius.
 - Реализуйте геттер и сеттер для celsius, где сеттер проверяет, что температура не может быть ниже -273.15°C (абсолютный ноль).
 - Добавьте свойство fahrenheit (геттер), которое возвращает температуру в Фаренгейтах (формула: °F = °C * 9/5 + 32).

temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
temp.celsius = -300    # Должно вызвать ValueError
'''