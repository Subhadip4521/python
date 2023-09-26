class employee:
    company= 'google'
    def status(self):
        print("I am an employee")

class programmer(employee):
    company='youtube'

    def status(self):
        print("I am a programmer.")

e=employee()
print(e.company)
e.status()
p=programmer()
print(p.company)
p.status()