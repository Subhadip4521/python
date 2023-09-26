f= open('test.txt', 'r')        #if we dont specify the mode it will take reading mode by default.

data= f.read()
# data= f.read(5)                 #reads first 5 characters of the file
print(data)
f.close()