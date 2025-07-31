class Obj:
    data_int = 0
    data_str = "0"

    def __init__(self, *data, **also_data):
        if type(data[0]) == int and type(data[1]) == int:
            print(data[0],data[1])
            self.data_int = data[0] + data[1]
        elif type(data[0]) == (str or chr) and type(data[1]) == (str or chr):
            self.data_str = data[0] + data[1]
        elif (type(data[0]) == int) and (type(data[1]) == str) or (type(data[0]) == str) and (type(data[1]) == int):
            if data[0] is int and data[1] is str:
                self.data_int, self.data_str = data[0], data[1]
            else:
                self.data_int, self.data_str = data[0], data[1]

    def output(self):
        print(self.data_int, self.data_str, sep = '\t')





a = Obj(33,'hello',56,88)
a.output()

#dat = list(input("user input, use ' ' or ',' : ").replace(' ', ',').split(',')) слишком много перепроверять. 
#                                                                                Будет, пока что, урезанный функционал



'''
2) Напишите программу, в которой описан класс со следующими свойствами. 
В классе описан конструктор, которому в качестве аргументов (помимо первой ссылки на создаваемый объект)
 передаются текст и целое число, причем в произвольном порядке.
Число и текст присваиваются как значения определенным полям. 
Если переданы два текстовых
значения, то создается только текстовое поле со значением, получающимся объединением значений аргументов. 
Если аргументами переданы два числовых поля, то у объекта будет только поле с целочисленным значением, 
равным сумме значений аргументов. В иных случаях поля для объекта не создаются. 
Создать на основе класса объекты и проверить функциональность кода.  
(Нужно вспомнить про *args и **kwargs)
'''
