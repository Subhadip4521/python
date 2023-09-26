num=int(input("Enter a number: "))
temp=num
n=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**n
    temp=temp//10

if num==sum:
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")

