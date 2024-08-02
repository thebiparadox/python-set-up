string = input('Enter string: ') #gets string from user

import re #imports regex module
regex = 'bob' #defines regex as bob
match = re.findall(regex, string) #finds all instances of 'bob' in string

bobCount = 0 #establishes counter

for count, bob in enumerate(match, start = 0): #counts number of 'bob' items in list
    bobCount = count + 1
print('Number of times bob occurs is:', bobCount) #prints number of 'bob' items in list
