def multable(num):
    i=1
    while i<=10:
        print(f"{num}X{i}={num*i}")
        i=i+1
        

number=int(input("Enter a number: "))
print("Multiplicatiuon table:--->>>>")
m=multable(number)

