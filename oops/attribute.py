class sample:
    a= 'subhadip'

name= sample()
name.a='dip'

print(sample.a)     #class attribute will not change even after creating instance attribute
print(name.a)