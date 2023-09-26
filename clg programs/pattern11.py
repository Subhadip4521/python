''' * * * * * * * * *  
      * * * * * * *
        * * * * *
          * * *
            *       '''

n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    for j in range(0,i-1):
        print(" ",end=" ")
    for k in range(0,(2*n-2*i+1)):
        print("*",end=" ")
    print(" ")