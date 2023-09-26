
with open('slang.txt') as f:
    slang=f.read()
    
slang=slang.replace('donkey','######')
with open('slang.txt','w') as f:
    f.write(slang)