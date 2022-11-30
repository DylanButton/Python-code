

guessNum = 0
import random
randomNum = random.randint(1,10)
run = True
while run == True:
    guessNum=int(input("I have generated a random number, guess what that random number is!"))

    if randomNum == guessNum:
        print("Correct, Here is your golden star")
        break
    elif randomNum < guessNum:
        print("The number you guessed is to large, try again!")
    elif randomNum > guessNum:
        print("The number you guessed is to small, try again!")
    else:
        print("invalid dataset")
        
