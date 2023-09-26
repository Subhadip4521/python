class employee:
    def __init__(self,name,company,salary):
        self.name= name
        self.company= company
        self.salary=salary
        print("The employee background is creating--->")

    def getDetails(self):
        print(f"Name of the employee is {self.name}")
        print(f"Name of his company is {self.company}")
        print(f"Salary is {self.salary}")

sd= employee("subhadip Das","Google",100000)
sd.getDetails()