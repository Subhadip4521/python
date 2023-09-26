a=set()
a.add(4)
a.add(6)
a.add(8)
a.add(10)
a.add((3,5,8))          # List and Dict can't be added in the set but touples can be added
print(a)

print(len(a))

a.remove(4)
print(a)

print(a.pop())

print(a.union({8,11}))


print(a.intersection({8,11}))


print(a.clear())