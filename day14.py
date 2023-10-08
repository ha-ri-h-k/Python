
#Grret user
def greet_user(name):
    print("Hello, "+name+"!\nWelcome to our program.")

greet_user("Hari")

######################### return
def add_number(a,b):
    sum_result = a+b
    return sum_result
result = add_number(4,2)
print("Result:",result)
############################
def greet_person(name,msg="Hello, nice to meet you!"):
    print(msg,name)

greet_person("Alice")
greet_person("Bob","Hey there")
###############################
def per_info(name, age, city):
    print("Name", name)
    print("Age", age)
    print("City", city)
per_info(name="Alice", age=30, city="New york")
##########################factorial
def fact(num):
    if num==0:
        return 1
    else:
        return num *fact(num-1)

n = int(input("Enter the number:"))
r= fact(n)
print(f"The factorial of {n} is {r}")

