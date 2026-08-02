"""Make a program that:
Takes a student's name.
Takes marks.
Saves both into student.txt.
Reads the file.
Prints the saved information."""

name = input ("Enter your name : ")
marks = input ("Enter your marks : ")

with open ("student.txt " , "w") as file:
    file.write("Name : " + name + "\n")
    file.write("Marks : " + marks)
    
with open ("student.txt " , "r") as file:
    data = file.read()
    
    
print("\nSaved Information")
print(data)
