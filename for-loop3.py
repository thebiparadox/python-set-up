end = int(input("Enter a number here: ")) + 1 #gets a number from user input

result = 0

for x in range(0, end): #sums values 1 through end, inclusive
    result = result + x

print(result) #prints the resulting value