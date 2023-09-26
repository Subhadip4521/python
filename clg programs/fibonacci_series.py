terms= int(input("Enter the terms of the series: "))

num01=0
num02=1
count=0

if terms<=0:
    print("Enter a positive integer...")
elif terms==1:
    print("FIBONACCI series: ",num01)
else:
    print("FIBONACCI series: ",end=" ")
    print(num01,end=" ")
    print(num02,end=" ")
    while count<terms-2:
        num=num01+num02
        print(num,end=" ")
        num01=num02
        num02=num
        count+=1
