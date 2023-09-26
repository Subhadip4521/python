def temp(fahrenheit):
    fahrenheit=(celsius*(9/5)+32)
    return  fahrenheit

celsius= int(input("Enter temperature in celsius: "))
temp(celsius)
print("The temperature in fahrenheit is:",temp(celsius))

