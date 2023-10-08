g_var =10
def ex_function():
    l_var=20
    print("inside the function - local_var",l_var)
    print("Inside the function - global_var",g_var)

print("Outside the function - global_var",g_var)
print("inside the function - local_var",l_var)
print("\n")
ex_function()

##################3
def add_num(a,b):
    result = a+b
    return result
sum_result = add_num(5,7)
print("Sum",sum_result)

#################################
def get_greeting(name):
    greeting = "Hello, " + name + "!"
    return greeting


print(get_greeting("Alice"))


###################
attempt = 0
def pswd_chec(pswd):
    global attempt
    if len(pswd) >=8 and
            any(char.islower() for char in pswd) and
            any(char.islower() for char in pswd) and
            any(char.isdigit() for char in pswd) and
            ' ' not in pswd:
        return True
    return False
while attempt < 3:
    u_pswd = input("Enter your password:")
    if pswd_chec(u_pswd):
        print("Password accepted")
        break
    else
        attempt +=1
        print("Invalid password. Please try again")

if attempt == 3:
    print("Maximum no.of attempts reached. Exiting")