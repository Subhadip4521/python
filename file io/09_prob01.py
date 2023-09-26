with open('poems.txt') as f:
    data= f.read()
    if 'Twinkle' in data:
        print("Twinkle is present.")
    else:
        print("Twinkle is not present.")
