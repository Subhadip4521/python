class employee:
    company= 'Google'
    salary= 10000
    def get_salary(self,signature):
        print(f"My company is {self.company}\nMy salary is {self.salary}\n{signature}.")

sd= employee()
dip= employee()

# sd.company='facebook'
print(sd.company)
print(dip.company)

employee.company= 'youtube'

print(sd.company)
print(dip.company)

sd.salary= 20000
dip.salary=15000

print(sd.salary)
print(dip.salary)

sd.get_salary("Thanks!")     # ---> employee.get_salary(sd)


