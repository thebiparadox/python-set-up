#this is a guess the number game

import random #gets random module

secretNumber = random.randint(1, 20) #generates random number between 1 and 20

print('I am thinking of a number between 1 and 20.') #explains premise of the game

#ask the player to guess 6 times

for guessesTaken in range (1, 7):
    print('Take a guess.') #prompts user for input
    guess = int(input()) #gets input from user

    if guess < secretNumber: #evaluates user input against the chosen random number
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #this condition is the correct guess

if guess == secretNumber: #reveals answer and guess #
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
