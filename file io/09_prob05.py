with open('slang.txt') as f:
    slang=f.read()
    
words=['donkey','bc','mc']
for word in words:
    slang=slang.replace(word,'######')
    with open('slang.txt','w') as f:
        f.write(slang)