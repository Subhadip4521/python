dictonary={
    'ami':'I',
    'akjon':'a or an',
    'valo':'good',
    'daktar':'doctor',
    'hote chai':'want to be'
}

print("Enter word from the given list: ",list(dictonary.keys()))
user=input("Enter a bengali word: ")
print("The English meaning of your word is: ",dictonary.get(user))