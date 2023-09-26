n=int(input("Enter the number of rows: "))

for i in range(n-1):
    print("  " * (n-i-1),end="")
    print("* " * (2*i -1),end="")
    print("  " * (n-i-1))
for i in range(n-1,0,-1):
    print("  " * (n-i-1),end="")
    print("* " * (2*i -1),end="")
    print("  " * (n-i-1))
