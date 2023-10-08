str1= "Hello"
str2 = "World"
res = str1+" "+str2
print(res)
##############string index################
msg  = "Python"
print(msg[0])
print(msg[2])
###################################3
txt = "Hello"
print(len(txt))

##############################
msg = "Python is Awesome"
print(msg.upper())
print(msg.lower())
############################
txt ="   Hello   "
print(txt.strip())
##########################3
msg = "Python is fun"
print(msg.find("fun"))
########################
txt = "Hello World!"
new_txt = txt.replace("Hello","Hi")
print(new_txt)
###string formatting
name = "Hari"
age = 22
print(f"My name is {name} and I am {age} years old.")
############string format()######################
item ="apple"
price =1.25
print("The price of {} is ${:.2f}".format(item,price))
###################
msg = "He said, \"Hello!\""
print(msg)
###############string to list ################3
txt = "Hello"
char_list = list(txt)
print(char_list)
##########list to word##############
w_list = ['p','y','t','h','o','n']
word = "".join(w_list)
print(word)
###string reverse############
def re_str(input_str):
    reversed_str = input_str[::-1]
    return reversed_str
user_input = input("Enter a string\n")
reversed_input = re_str(user_input)
print("Reversed string:",reversed_input)
###############################
char1 = input("Enter the string")
char = char1.lower()
if char[0] in ['a','e','i','o','u']:
     print("Vowel")
else:
    print("Not vowel")