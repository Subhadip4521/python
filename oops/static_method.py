class employee:
    company= 'Google'
    salary= 10000
    def get_salary(self):
        print("My salary is 500k.")

    @staticmethod
    def greet():
        print("Good moring, SD")

sd= employee()
sd.get_salary()
sd.greet()
