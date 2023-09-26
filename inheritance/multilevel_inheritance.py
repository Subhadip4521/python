class employee:
    company= 'masterclass'

class person(employee):
    print("I am an employee.")

class freelancer(person):
    company = 'upwork'
    level=0
    def upgradelevel(self):
        self.level= self.level+1
        print(p.level)

        

class programmer(freelancer):
    name='sd'

p=programmer()
print(p.company)
# print(p.level)
p.upgradelevel()
print(p.level)