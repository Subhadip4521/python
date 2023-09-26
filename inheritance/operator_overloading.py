class number:

    def __init__(self, num):
        self.num= num

    def __add__(self, num02):
        print("let's add")
        return self.num+ num02.num

    def __mul__(self, num02):
        print("Let's multiply")
        return self.num* num02.num

n1=number(3)
n2=number(48)

sum=n1+n2
print(sum)

mul=n1*n2
print(mul)