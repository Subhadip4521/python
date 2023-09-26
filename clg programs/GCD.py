# import math
# print("The GCD of the given numbers are: ",math.gcd(3, 6))


num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

if num1>num2:
    smaller=num2
else:
    smaller=num1

for i in range(1,smaller+1):
    if (num1%i==0 and num2%i==0):
        gcd=i
    
print("The GCD of the given two numbers are: ",gcd)
