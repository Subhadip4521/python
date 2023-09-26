
text=input("Enter the text: ")
if('make a lot of money' or 'Make a lot of money' in text):
    spam=True
elif('buy now' or 'Buy now' in text):
    spam=True
elif('click this' or 'Click this' in text):
    spam=True
elif('subscribe now' or 'Subscribe now' in text):
    spam=True
else:
    spam=False

if(spam):
    print("This is a spam text.")
else:
    print("This is not a spam text.")