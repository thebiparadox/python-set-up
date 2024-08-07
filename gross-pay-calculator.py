import sys #gets sys module

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

def computePay(hours, rate): #function to calculate pay
    if hours <= 40.0: #calcuates rate under 40 hours worked
        pay = round(hours * rate)
        return pay
    elif hours > 40.0: #calculates rate over 40 hours worked
        regularPay = 40.0 * rate
        overtime = hours - 40
        overtimePay = overtime * (rate * 1.5)
        pay = round(regularPay + overtimePay)
        return pay

print("Pay:", computePay(hours, rate)) #prints result of function computePay()