def num(n):
    if (n%7==0 and n%5!=0):
        print(f"{n} is divisible by 7 and not divisible by 5.")
        
x= int(input("Enter how many numbers you want to check: "))

for i in range(1,x+1):
    number=int(input(f"Enter the number {i}: "))
    num(number)
