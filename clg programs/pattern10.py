'''4 3 2 1
   3 2 1
   2 1
   1'''

n= int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(n-i+1,0,-1):
        print(j,end=" ")
    print(" ")