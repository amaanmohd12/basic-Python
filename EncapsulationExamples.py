class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
    def inc_salary(self,amount):
        self._salary+=amount
    def display(self):
        return self._salary
e=Employee("Amaan",15000)
e.inc_salary(5000)
print(e.display())
class Account:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
    def display(self):
        return self._balance

acc=Account(123,15000)
acc.deposit(5000)
print(acc.display())
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=Student("Amaan",21)
s2=Student("Muaaz",20)
s1.display()
s2.display()
