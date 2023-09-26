# without using recursion

# def addition(num):
#     s=(num * (num+1))/2
#     return s

# number=int(input("Enter n term for sum of natural numbers: "))
# addition(number)
# print(f"The sum of first {number} natural numbers are:",int(addition(number)))


# using recursion--->>>>>
def sum(n):
    if n==1:
        return n
     
    return n+ sum(n-1)

number=int(input("Enter n term for sum of natural numbers: "))
sum(number)
print(f"The sum of first {number} natural numbers are:",int(sum(number)))

