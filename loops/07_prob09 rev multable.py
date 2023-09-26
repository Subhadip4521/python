print("**********This is a reverse multiplication table********")
num=int(input("Enter a number: "))
print("Reverse Multiplication table:---->>")

# i=10
# while(i>=1):
#     print(f"{num}X{i}={num*i}")
#     i=i-1

for i in range(10,0,-1):
    print(f"{num}X{i}={num*i}")

