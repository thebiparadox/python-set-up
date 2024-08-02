import sys

hoursInput = input('Enter Hours: ') #user inputs hours and rate
try:
    hours = float(hoursInput)
except:
    print('Error, please enter numeric input')
    sys.exit()
rateInput = input('Enter Rate: ')
try:
    rate = float(rateInput)
except:
    print('Error, please enter numeric input')
    sys.exit()

if hours <= 40.0: #calcuates rate under 40 hours worked
    pay = hours * rate
elif hours > 40.0: #calculates rate over 40 hours worked
    pay = hours * (rate * 1.5)

print("Pay:", round(pay)) #rounds to the nearest integer and prints result