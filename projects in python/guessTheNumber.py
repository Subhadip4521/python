import random

print("**********************\n")
print("Welcome to the game by SUBHADIP DAS...")
randNumber= random.randint(1, 1000)
# print(randNumber)

userGuess=None
guess=0
while userGuess!=randNumber:
    userGuess= int(input("\nPlease guess a number between 1 and 1000: "))
    guess+=1
    if userGuess==randNumber:
        print("Hurray! You guessed it right   :)")
        print(f"You did a right guess in {guess} attempt(s).")
        break
    else:
        print("Oops! You guessed it wrong   :(")
        if userGuess<randNumber:
            print("Higher number please--> ")
        if userGuess>randNumber:
            print("Lower number please--> ")

with open('highscore.txt','r') as f:
    highscore= int(f.read())

if guess<highscore:
    print("You have broken the highscore, CONGRATS---")
    print("**********************\n")
    with open('highscore.txt', 'w') as f:
        f.write(str(guess))
else:
    print(f"The highscore was {highscore}")
    print("**********************\n")