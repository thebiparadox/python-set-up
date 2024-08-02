import sys #gets sys module

while True: #creates infinite loop that can only be exited by typing exit
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')