string = input('Enter a string here: ') #gets string from user

alphaStringCounter = 0 #counter

for letter in string:
    if letter == 'a':
        alphaStringCounter = alphaStringCounter + 1
        continue
    elif letter == 'b':
        alphaStringCounter = alphaStringCounter + 1
        continue
    elif letter == 'c':
        alphaStringCounter = alphaStringCounter + 1
    else:
        break

print('Longest substring in alphabetical order is:', alphaStringCounter)