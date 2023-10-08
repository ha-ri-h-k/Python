#Fibonacci
def is_fibinacci(n):
    n1 = 1
    n2 = 1
    n3 = 0
    if n == 0 or n == 1:
        print( n,"is a fibonacci number")
    else:
        while n3 < n:
            n3 = n1 + n2
            n2 = n1
            n1 = n3
        if n3 == n:
            print(n,"is a fibonacci number")
        else:
            print(n,"is not fibonacci number")

n = int(input("Enter the number to be checked:"))
is_fibinacci(n)
#vowels count
def count_vowels(str1):
    count =0
    str2 = str1.lower()
    for i in str2:
        if i== 'a' or i=='e'or i == 'i'or i=='o'or i=='u':
            count +=1
    if count != 0:
        print("No of vowels in string",str1,"is",count)
    else:
        print("There is no vowels in the string",str1)

str1=str(input("Enter the string"))
count_vowels(str1)
#palindrome
def is_palindrome_tuple(tup):
    if tup[::-1] == tup:
        print(tup,"is palindrome")
    else:
        print(tup,"is not palindrome")
tup = tuple(input("Enter the input"))
is_palindrome_tuple(tup)