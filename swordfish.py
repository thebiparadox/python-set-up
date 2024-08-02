while True: #condition is always true until break statement
    print('Who are you?') 
    name = input() #gets name from user input
    if name != 'Joe': #compares user input to admin name. If they don't match, loop continues
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input() #gets password from user imput
    if password == 'swordfish': #compares user imput to password. If they match, breaks out of loop
        break

print('Access granted.')