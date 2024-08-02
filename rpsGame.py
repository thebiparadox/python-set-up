#rock, paper scissors game

import random, sys #imports random and sys modules

print('ROCK, PAPER, SCISSORS')

wins = 0 #these variables keep track of the number of wins, losses, and ties.
losses = 0
ties = 0

while True: #the main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break out of the player input loop.
    print('Type one of r, p, s, or q.')

    if playerMove - 'r': #displays what the player chose
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove = 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1, 3) #displays what the computer chose
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove: #displays and records the win/loss/tie
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1 
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1  
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1  
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1  
