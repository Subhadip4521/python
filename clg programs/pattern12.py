'''         *  
          * * *
        * * * * *
      * * * * * * *
        * * * * *
          * * *
            *       '''

n= int(input("Enter the number(odd number) of rows: "))
if n%2==0:
    print("Invalid number...")
else:    
    y=n//2
    x=n-y

    for i in range(1,x+1):
        for j in range(0,n-i):
            print(" ",end=" ")
        for k in range(0,(2*i-1)):
            print("*",end=" ")
        print(" ")
    for a in range(1,y+1):
        for b in range(0,a+y):
            print(" ",end=" ")
        for c in range(0,(2*y-2*a+1)):
            print("*",end=" ")
        print(" ")
