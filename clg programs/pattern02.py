'''1  
   2 2
   3 3 3
   4 4 4 4
   5 5 5 5 5'''

n= int(input("Enter number of rows: "))
a=1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(f"{a}",end=" ")
    a=a+1
    print(" ")