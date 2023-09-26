class employee:
    company= 'masterclass'

class freelancer:
    company = 'upwork'
    level=0
    def upgradelevel(self):
        self.level= self.level+1
        print(p.level)

        

class programmer(employee, freelancer):
    name='sd'

p=programmer()
print(p.company)
# print(p.level)
p.upgradelevel()
print(p.level)