my_set = {1, 2, 3, 4, 5}
print(my_set)
#############################
an_set =set([5, 6, 7, 8, 9])
print(an_set)
###########adding elements to set #########
fruit = {'apple', 'banana', 'orange'}
fruit.add('grape')
print(fruit)
################removing elements form set####################3
fruit = {'apple','banana','orange'}
fruit.remove('apple')
print(fruit)
###############set operations #####################
#union
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)
##########intersection####################
set1 = {1,2,3}
set2 = {3,4,5}
intersection_set = set1.intersection(set2)
print(intersection_set)
######Difference######33
set1 = {1,2,3}
set2 = {3,4,5}
difference_set = set1.difference(set2)
print(difference_set)
###############################
set1 = {1,2}
set2 = {1,2,3,4}
print(set1.issubset(set2))
print(set2.issuperset(set1))
#####symmetric set ###########
set1 = {1,2,3}
set2 = {3,4,5}
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set)
################################
set_a = {1, 3, 5, 7, 9}
set_b = {0,2, 4, 6, 8}
print("Set A:", set_a)
print("Set B", set_b)
union_set = set_a.union(set_b)
print("\nUnion:", union_set)
intersection_set = set_a.intersection(set_b)
print("\nIntersection", intersection_set)
diff_set = set_a.difference(set_b)
print("\nDiffernece with a to b", diff_set)
diff2_set = set_b.difference(set_a)
print("\nDifference with b to a", diff2_set)
sym_diff_set = set_a.symmetric_difference(set_b)
print("\nSymmetric differnce with a and b", sym_diff_set)
