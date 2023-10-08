# Sets and Related Operations
# Question 1:  Create a program that takes two lists as input and implements a
# function to find the common elements between them using sets. Then, create a
# menu-driven interface allowing the user to perform set operations like union,
# intersection, and difference on these lists.

def common_ele(set1,set2):
    # set1 =set(list1)
    # set2 =set(list2)
    intersection = set1.intersection(set2)
    return intersection


def value_input(n,list3):

    for i in range(n):
        values1 = input("Enter the values")
        #values2 = input("Enter the values")

        list3.append(values1)
        #list2.append(values2)
def union(set1,set2):
    union_list = set1.union(set2)
    return union_list
def differ(set1,set2):
    diff_list = set1.differ(set1,set2)
    return diff_list
# def menu():
#     print("MENU\n")
#     print("1.UNION")
#     print("2.INTERSECTION")
#     print("3.DIFFERENCE\n")
#     c = int(input("Enter your choice"))
#     if c == 1:
#         print(union(set1, set2))
#     elif c == 2:
#         print(intersection(set1, set2))
#     elif c == 3:
#         print(common_ele(set1, set2))
#     elif c == 4:
#         print(differ(set1, set2))
#     else:
#         print("Invalid")
def main():
    list1 = []
    list2 = []
    n1= int(input("Enter the 1st list count"))
    n2=int(input("Enter the 2nd list count"))
    print("Values for list 1")
    value_input(n1,list1)
    print("Values for list 2")
    value_input(n2,list2)
    print("list A:",list1)
    print("list B:",list2)
    set1 = set(list1)
    set2 = set(list2)
    print("COMMON ELEMENTS",common_ele(set1,set2))
    #menu()
    print("MENU\n")
    print("1.UNION")
    print("2.INTERSECTION")
    print("3.DIFFERENCE\n")
    c = int(input("Enter your choice"))
    if c == 1:
        print("UNION:",union(set1, set2))
    # elif c ==2:
    #     print("INTERSECTION:",intersection(set1,set2))
    elif c == 2:
        print("INTERSECTION:",common_ele(set1,set2))
    elif c == 3:
        print("DIFFERENCE:",differ(set1,set2))
    else:
        print("Invalid")


main()



# Dictionaries and Related Operations
# Question 2:  Write a Python program that reads a text file containing a large amount of text.
# Implement a function to count the occurrences of each word in the file and store the word frequencies
# in a dictionary. After processing the entire file, display the top 10 most frequent words along with their counts.


# File Handling
# Question 3:  Develop a program that takes a CSV file as input and processes its data.
# The file contains information about employees, with columns like name, age, salary, and department
# . Implement a function that calculates the average salary of employees in each department and writes the result to a new CSV file.




# Functions and Function Parameters
# Question 4:  Write a Python program that simulates an online shopping cart.
# Implement a function to add items to the cart along with their quantities.
# Create functions to calculate the total cost, apply discounts, and calculate the final payable amount based on user input.





# Global Variables and Variable Scope
# Question 5:  Design a program that tracks the score of an online multiplayer game.
# Create a global dictionary to store the scores of different players.
# Implement functions to update the scores, add new players, and display the top 5 players with the highest scores.