#tupple accessing elements
my_tupple = (1,2,3,'hello','world')
print(my_tupple[0])
print(my_tupple[-1])

#tupple slicing
my_tupple = (1,2,3,'hello','world')
print(my_tupple[1:4])
print(my_tupple[::2]) #print(my_tupple[0:5:2])

##Tupple concatenation
tuple1 = (1,2,3,)
tuple2 = ('hello','world')
cont_tuple = tuple1 + tuple2
rept_tuple = tuple1 * 3
print(cont_tuple)
print(rept_tuple)

####Tuple length and membership
my_tupple = (1,2,3,'hello','world')
print(len(my_tupple))
print('hello'in my_tupple)
print('python'in my_tupple)

#unpacking tuples
my_tupple = (1,2,3)
a,b,c = my_tupple
print(a)
print(b)
print(c)

#methods
my_tupple = (1,2,2,4,3,3)
count_2 = my_tupple.count(2)
index_3 = my_tupple.index(3)
print(count_2)
print(index_3)

# Write a program that takes a tuple of numbers as input and prints the sum of all the elements.?
my_tuple = eval(input("enter the value"))
sum =0
for num in my_tuple:
    sum += num
#for i in range(0,len(my_tuple)+1)
    #sum = sum + my_tupple
#print(sum)
print(sum)