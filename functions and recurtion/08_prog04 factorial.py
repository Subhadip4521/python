def factorial(n):
    
    product=1
    for i in range(n):
        product=product*(i+1)
    print(product)

num=int(input("Enter a number for getting factorial: "))
factorial(num)
