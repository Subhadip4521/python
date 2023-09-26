class employee:
    salary= 6000
    bonus= 500

    @property
    def totalSalary(self):
        return self.salary+self.bonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.bonus= val - self.salary


e= employee()
print(e.salary)
print(e.bonus)
print(e.totalSalary)

e.totalSalary=6300
print(e.salary)
print(e.bonus)
