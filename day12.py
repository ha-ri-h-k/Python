student_ages = {"Alice": 25, "Bob": 23, "Charlie": 22}
print(student_ages)
bob_age = student_ages["Bob"]
print(bob_age)
student_ages["David"]=20
student_ages["Alice"]=26
print(student_ages)

num_students = len(student_ages)
print(num_students)

if 'Alice' in student_ages:
    print("Alice is in the dictionary")
else:
    print("Alice is not in the dictionary")

del student_ages["Charlie"]
print(student_ages)

for student in student_ages:
    age = student_ages[student]
    print(f"{student} is {age} years old.")


bob_age = student_ages.get("Bob","Age not available")
grace_age = student_ages.get("Grace","Age not available")
print(bob_age)
print(grace_age)

all_students = student_ages.keys()
all_ages = student_ages.values()
all_entries = student_ages.items()
print(all_students)
print(all_ages)
print(all_entries)
################3
bio_data ={"Fname":"Hari","Lname":"HK","age":22,"DOB":'09/02/2001',"Qualification":"Btech","Mail_id":"harihk0666@gmail.com","ph_no":9562149972}
for i in bio_data:
    data = bio_data[i]
    print(f"{i} : {data}")
#print(bio_data)