'''* * * * *
   * * * *
   * * *
   * *
   *         '''

n= int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(0,n-i+1):
        print("* ",end="")
    print(" ")


