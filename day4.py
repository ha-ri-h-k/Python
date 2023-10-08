a = 10
b = 5
c = 3.14
d = 2.5
e = 2 + 3j
f = 1 - 2j
sum1 = a + b
sum2 = c + d
sum3 = e + f
print("a + b =", sum1)
print("c + d =", sum2)
print("e + f =", sum3)


fname = "Hari"
lname = "HK"

print(fname)
print(lname)

#concatination
fullname = fname + " " + lname
print("Full name = ", fullname)

#repetition
rep = 2 * fullname
print("Repeated text = ",rep)

#string indexing and slicing
print(fullname[0])
print(fullname[3])
print(fullname[1:4])
print(fullname[::-1])

#Manipulation
u_fullname = fullname.upper()
print(u_fullname)
l_fullname = fullname.lower()
print(l_fullname)
repl_st = fullname.replace("HK", "Krishnan")
print(repl_st)


