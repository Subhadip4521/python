class vector:
    def __init__(self, vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=0
        for  i in self.vec:
            str1 += f"{i}a{index} +"
            index +=1
        return str1[:-1]

v= vector([1,5,7])
print(v)