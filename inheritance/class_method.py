class employee:
    salary= 100

    # def changeSalary(self, sal):
    #     self.__class__.salary= sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary= sal

e=employee()
print(e.salary)
e.changeSalary(600)
print(e.salary)
print(employee.salary)
