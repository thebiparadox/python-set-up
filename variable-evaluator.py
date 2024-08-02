#establish variables for testing

varA = int(input('Enter a number: '))
varB = int(input('Enter a number: '))

#evaluates variables for type and value

if isinstance(varA or varB, str):
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    print('smaller')
