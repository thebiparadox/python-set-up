def collatz(number): #defines function
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

input_number = input('Please enter a number: ')

try:
    converted_number = int(input_number)
except ValueError:
    print('You must enter a number')

while True:
    result = collatz(converted_number)
    if result > 1:
        print(result)
        converted_number = result
    elif result == 1:
        print(result)
        break

print('End!')

