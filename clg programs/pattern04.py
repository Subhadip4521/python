''' 1  
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5'''

n= int(input("Enter number of rows: "))

for i in range(1, n+1):
    for j in range(0,n-i):
        print("",end=" ")
    for k in range(0, i):
        print(i,end=" ")
    print(" ")