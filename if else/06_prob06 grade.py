marks=float(input("Enter your marks: "))

if marks>=90 and marks<=100:
    Grade='EX'
elif marks>=80:
    Grade='A'
elif marks>=70:
    Grade='B'
elif marks>=60:
    Grade='C'
elif marks>=50:
    Grade='D'
else:
    Grade='F'
print("Your grade is ",Grade)