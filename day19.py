# class ElectricCar(Car)
#     def __init__(self,make,model,year,batt_cap):
#         super().__init__
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.grdnyear = year


x = student("Hari", "HK", 2019)
print(x.grdnyear)
print(x.firstname, x.lastname)

##############3
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
##################3

class BankAc:
    def __init__(self):
        self.bal = 0
def dep(self,amount):
    self.bal+= amount
def withdraw(self,amount):
    if amount <= self.bal:
        self.bal -= amount
        return amount
    else:
        return "Insufficent funds."
print("1.DEPOSIT")
print("2.WITHDRAW")
n = int(input("Enter your choice (1/2)"))
ac= BankAc()
print("Balance:"ac.bal)
ac.dep(1000)
print("Bal after deposit:",ac.bal)

