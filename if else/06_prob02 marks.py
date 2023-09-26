marks1=float(input("Enter the marks of Maths: "))
marks2=float(input("Enter the marks of physics: "))
marks3=float(input("Enter the marks of chemistry: "))

print("Your marks in maths is ",marks1)
print("Your marks in physics is ",marks2)
print("Your marks in chemistry is ",marks3)

total_percentage=((marks1+marks2+marks3)/3)
print("Your total percentage is",total_percentage)

if(marks1>=33 and marks2>=33 and marks3>=33 and total_percentage>=40):
    print("You are passed")
else:
    print("You are failed")