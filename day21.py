#Syntax error
print("Hello world) #missing closinq
x=10
    y=20 #indentation error
#####################3

n1 = 10
n2 = 0
res = n1/n2   # division by zero
#################3

#Logical error
r = 5
area = 2 * 3.14 * r
print(area)
###########################
try:
    n1 = int(input("Enter a number"))
    n2 = int(input("Enter another number:"))
    res = n1 / n2
    print("Result:",res)
except ValueError:
    print("Invalid input.Please enter a valid integer")
except ZeroDivisionError:
    print("Cannot divide by zero.")
#################################
try:
    path = "C:/Users/jeffi/OneDrive/Desktop/example.txt"
    file = open(path, "r")
    num = int(file.read())
    res = 100 / num
    print("Result", res)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Invalid input please check the content of the file")
except ZeroDivisionError:
    print("Cannot divide by zero.")
##################################
try:
    n1 = int(input("Enter a number"))
    n2 = int(input("Enter another number:"))
except ValueError:
    print("Invalid input.Please enter a vaild integer")
else:
    res = n1/n2
    print("Result ",res)
#########################

try:
    path = "C:/Users/jeffi/OneDrive/Desktop/data.txt"
    file = open(path,"r")
except FileNotFoundError:
    print("File not found")
finally:
    file.close() #ensunring the file os close

#custom error
class CustomError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
try:
    age = int(input("Enter your age"))
    if age < 0:
        raise CustomError("Age cannot be negative.")
except ValueError:
    print("Invalid input.Please enter a valid integer")
except CustomError as ce:
    print(ce)