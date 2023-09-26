class employee:
    company= 'masterclass'

class person(employee):
    print("I am an employee.")
    company='india'
    level=2
    def upgradelevel(self):
        self.level= self.level+1
        print(p.level)

class freelancer(person):
    company = 'upwork'
    level=0
    
    def upgradelevel(self):
        super().upgradelevel()
        self.level= self.level+1
        
        
class programmer(freelancer):
    name='sd'
    

p=programmer()
f=freelancer()
print(p.company)
print(f.company)
# print(p.level)
f.upgradelevel()
p.upgradelevel()
print(p.level)
p.upgradelevel()