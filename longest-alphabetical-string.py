s = input('Please input a string of letters: ')

s = s + ''
substring = ''
currentString = 0
previousLongestString = 0
longestSubstring = ''

for count, i in enumerate(s):
    substring = substring + i
    currentString = currentString + 1
    thisElement = ord(i)
    nextElement = ord(s[(count + 1) % len(s)])
    if thisElement >= nextElement:
        if len(substring) > previousLongestString:
            previousLongestString = currentString
            longestSubstring = substring
        substring = ''
        currentString = 0

print('Longest substring in alphabetical order is', longestSubstring)        
    
    





