print("**********This is a multiplication table********")
num=int(input("Enter a number: "))
print("Multiplication table:---->>")
for i in range(1, 11):
    # print(num, "x",i, "=", num*i)
    print(f"{num}X{i}={num*i}")
