def covt_to_int(input_str):
    try:
         n = int(input_str)
         return n
    except ValueError:
        return "Error:Invalid input.Please enter a valid integer."
print(covt_to_int("42"))
print(covt_to_int("Hello"))

############################################
#Multiple exceptions
def div_and_convert(a,b):
    try:
        res = int(a)/int(b)
        return res
    except ValueError:
        return "Error:Invalid input.Please enter vaild number."
    except ZeroDivisionError:
        return "Error:Division by zero is not allowed."

print(div_and_convert("10","2"))
print(div_and_convert("7","0"))
print(div_and_convert("hello","world"))
############################################################################

def process_list_item(input_list,index):
    try:
        result = input_list[index]
        return result
    except IndexError:
        return "Error:Index out of range.Please provide a vaild index"
    except TypeError:
        return "Error:Invalid input.Please provide a list and a valid index."
my_list =[1,2,3,4,5]
print(process_list_item(my_list,2))
print(process_list_item(my_list,10))
print(process_list_item("Hello",2))

#################################
def divide_num(a, b):
    try:
        result = a / b
        return result
    except Exception as e:
        return f"Error:{e}"


print(divide_num(10, 2))
print(divide_num(7, 0))
