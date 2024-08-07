print('Please think of a round number between 0 and 100!')

guess_counter = 0 #counts number of guesses
low_endpoint = 0 #initial low endpoint
high_endpoint = 100 #initial high endpoint

while True:
    guess = round((high_endpoint + low_endpoint) / 2) #bisection search for the secret number betwen 0 and 100
    guess_response = input('Is your secret number ' + str(guess) + '? Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.')
    if guess_response == 'h':
           high_endpoint = guess
    elif guess_response ==  'l':
          low_endpoint = guess
    elif guess_response == 'c':
        break
    else:
         print('I am sorry. I did not understand your response.')

print('Game over. Your secret number was:', guess) #prints secret number


