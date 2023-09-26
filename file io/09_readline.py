f= open('test.txt')        
data= f.readline()       # Reads 1st line       
print(data)
data= f.readline()       # Reads 2nd line and so on...       
print(data)
f.close()