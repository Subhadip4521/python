import os

oldfile= 'sample2.txt'
newfile= 'renamed_by_python.txt'

with open(oldfile) as f:
    content= f.read()

with open(newfile, 'w') as f:
    f.write(content)

os.remove(oldfile)