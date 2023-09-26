def greatest(num1, num2, num3):
    if num1>num3:
        print("The greatest number is:",num1)
    elif num2 > num3:
        print("The greatest number is:",num2)
    else:
        print("The greatest number is:",num3)

number1= int(input("Enter 1st number: "))
number2= int(input("Enter 2nd number: "))
number3= int(input("Enter 3rd number: "))

greatest(number1, number2, number3)
