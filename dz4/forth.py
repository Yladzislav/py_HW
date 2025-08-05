
class Employee:
    name : str
    _salary : int = 0

    def __init__(self, name, salary):
        self.name = name
        super().__getattribute__('_salary')
        self.set_salary(salary)

    def display_info(self):
        print(f'name : {self.name}',f'salary : {self.salary}', sep = '\n')

    def set_salary(self, new_salary):
        assert new_salary >= 0, ValueError
        super().__setattr__('_salary',new_salary) 

    def __setattr__(self, name, new_salary):
        assert name != '_salary', 'ALARM'
        super().__setattr__(name, new_salary)

    def __getattribute__(self, name):
        assert name != '_salary', 'ALARM'
        if name == 'salary':
            return super().__getattribute__('_salary')
        else:
            return super().__getattribute__(name)




class Manager(Employee):
    department : str

    def __init__(self, name : str, salary : int, department : str):
        super().__init__(name, salary)
        self.department = department 

    def display_info(self):
        super().display_info()
        print(f'department : {self.department}')
    

class Developer(Employee):
    programming_language : str
    
    def __init__(self,name : str, salary : int, programming_language : str):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f'prog language : {self.programming_language}')


a = Manager('Cate', 1000, 'HR')
a.salary = 10000    #pass, error not called, initial attribute did not change
#a._salary = 10000   #'ALARM'
#print(a.salary)     #pass, _salary getted
a.display_info()    #pass
#a.set_salary(-1000) #pass
a.set_salary(100)   #pass
print(a.salary)     #pass, 100
print()

b = Developer('Mark', 1000, 'Python')
b.salary = 10000    #pass, error not called, initial attribute did not change
#b._salary = 10000   #'ALARM'
#print(b.salary)     #pass, _salary getted
b.display_info()    #pass
#b.set_salary(-1000) #pass
b.set_salary(100)   #pass
print(b.salary) 

'''
4*)Создайте базовый класс Employee с атрибутами name, salary (защищённый) и методом display_info().
От него унаследуйте Manager (добавляет атрибут department) и Developer (добавляет programming_language).
Сделайте так, чтобы salary нельзя было изменить напрямую, но можно было через метод set_salary(), 
который проверяет, что зарплата не меньше 0.

dev = Developer("Alice", 5000, "Python")
dev.set_salary(-1000)  # Должно вызвать ошибку

'''