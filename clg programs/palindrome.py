num=int(input("Enter a number: "))
a=num
i=0
while(num>0):
    b=num%10
    i=i*10+b
    num=num//10
if(a==i):
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")