num=int(input("How many natural numbers do you want to make the factorial?---->> "))
fact=1
for i in range(1, num+1):
    fact=fact*i

print(f"The factorial of {num} is",fact)
