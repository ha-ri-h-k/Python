import math
n =25
result = math.sqrt(n)
print("Square root of ",n,"is",result)

n1 = 5
resultf = math.factorial(n1)
print("Factorial of ",n ,"is",resultf)

pi_value = math.pi
print("the value of pi is",pi_value)

import random
start =1
end = 10
random_no = random.randint(start,end)
print("Random interger between",start,"and",end,":",random_no)
fruit = ['apple',"bannan","cherry","orange"]
random_fruit = random.choice(fruit)
print("Random fruit from the list:",random_fruit)
import datetime
current_date_time = datetime.datetime.now()
print("Current date and time:", current_date_time)


import datetime
current_date_time = datetime.datetime.now()
print("Current date and time:", current_date_time)
date =datetime.date(2023,7,15)
formatted_date = date.strftime("%d-%b-%Y")
print("Formatted date:",formatted_date)

start_date = datetime.date(2023,7,13)
end_date = datetime.date(2023,7,15)

time_diff = end_date - start_date
print("Time difference in days:",time_diff.days)

#################
import os
currt_dir = os.getcwd()
print("Curent working directory:",currt_dir)

path = "C:/Users/jeffi/PycharmProjects/pythonProject"
file_in_dir = os.listdir(path)
print("File in the directory:",file_in_dir)

if os.path.exists(path) and os.path.isdir(path):
    print(path,"Exists and is a directroy.")
else:
    print(path,"Does not exist or is not a directory.")

