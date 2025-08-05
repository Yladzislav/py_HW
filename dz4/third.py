import random
class BankAccount:
    __balance : int = 0
    __account_number : int = 0

    def __init__(self, balance):
        self.__balance = balance
        self.__account_number = BankAccount.generate_account_number()

    @classmethod
    def create_account(cls,initial_balance : int):
       return cls(initial_balance)

    @staticmethod
    def generate_account_number():
        return random.randint(1000000000,9999999999)
    
    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number    
    
    @balance.setter
    def balance(self, new_balance):
        assert new_balance >= 0, ValueError
        self.__balance = new_balance

    
a = BankAccount.create_account(1000)
print(a.balance)
print(a.account_number)
a.balance = 500
print(a.balance)
a.balance = -100



'''
3) Реализуйте класс BankAccount:
 - Приватные атрибуты: __balance, __account_number.
 - Геттеры для баланса и номера счёта. Сеттер только для баланса (с проверкой, что баланс не может быть отрицательным).
 - Статический метод generate_account_number(), который возвращает случайный 10-значный номер счёта.
 - Метод класса create_account(cls, initial_balance), который создаёт аккаунт с сгенерированным номером.

account = BankAccount.create_account(1000)
print(account.balance)          # 1000
account.balance = -500          # ValueError

'''