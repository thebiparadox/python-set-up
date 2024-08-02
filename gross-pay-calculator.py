hours = input('Enter Hours: ') #user inputs hours and rate
rate = input('Enter Rate: ')
pay = float(hours) * float(rate) #converts input str to float and multiplies hours and rate to get pay
print("Pay:", round(pay)) #rounds to the nearest integer and prints result