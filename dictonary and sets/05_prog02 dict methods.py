mydict={
    "subha":"a good person",
    "marks":[24323],
    "dictonary":{"dip":"also a good person"},
    1:2
}

print(mydict.keys())
print(type(mydict.keys()))
print(list(mydict.keys()))


print(mydict.values())


print(mydict.items())


print(mydict)
updatedict={
    "single":"no girlfriend"
}
mydict.update(updatedict)
print(mydict)

print(mydict.get('subha'))      # .get returns none if the key is not present in the dictonary
print(mydict['subha'])          # [] throws an error as the key is not present in the dictonary 
