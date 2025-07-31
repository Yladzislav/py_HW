class Obj:

    def __init__(self, gibrish1, gibrish2, *to_be_ignored, **just_ignored):
        self.gib1 = gibrish1
        self.gib2 = gibrish2
        self.ignore = to_be_ignored
    
    def gib_call(self):
        print(self.gib1,self.gib2, sep = '\t')

    def ignored(self):
        print(self.ignore)

o1,o2,o3,o4 = Obj(32.4,'hello',12,33,443),Obj('32',5,12,33,"443"),Obj('32','hello',12,33,'443'),Obj({12:4},{'h':5},12,'33',443)

o1.gib_call()
o2.gib_call()
o3.gib_call()
o4.gib_call()

o1.ignored()

input_ = input("custom object class data, use ',' or ' ' for separation. Will take only 2 first values: ").replace(' ', ',').split(',')

custom = Obj(input_[0],input_[1])
custom.gib_call()

'''
1) Напишите программу, в которой описывается класс со следующими характеристиками.
 У класса есть конструктор, которому (кроме ссылки на объект вызова) передаются два значения.
 Эти значения присваиваются полям объекта класса. 
 В классе должен быть описан метод, при вызове которого отображаются значения полей класса. 
 Проверьте функциональность класса, создав на его основе несколько объектов.
'''