# opening a file
file_path = "example.txt"
file = open(r"C:\Users\jeffi\OneDrive\Desktop\example.txt", "r")#read
#file = open(r"C:\Users\jeffi\OneDrive\Desktop\example.txt", "w")#write
print(file)
#reading content
content = file.read()
print(content)
#write
file.write("Hello, this is an example of writing to a file\n")
file.write("Writing multiple lines.\n")
file.close()

#
# # opening a file
file_path = "example.txt"
file = open(r"C:\Users\jeffi\OneDrive\Desktop\example.txt", "w")
# #print(file)
#
#
# # content = file.read()
# # print(content)
#
# # line = file.readline()
# # print(line)
#with 'with' statements
file.write("Hello, this is an example of writing to a file\n")
file.write("Writing multiple lines.\n")
file.close()

file_path = "example.txt"
file = open(r"C:\Users\jeffi\OneDrive\Desktop\example.txt", "a")
file.write("This line will be added to the end of the file.\n")
file.close()
file_path = "example.txt"
with open(r"C:\Users\jeffi\OneDrive\Desktop\example.txt","r") as file:
    content = file.read()
    print(content)

with open(r"C:\Users\jeffi\OneDrive\Desktop\example.txt","w") as file:
    file.write("New data written using 'with' statements\n")

with open(r"C:\Users\jeffi\OneDrive\Desktop\example.txt","a") as file:
    file.write("This line is appended using 'with' statements\n")
