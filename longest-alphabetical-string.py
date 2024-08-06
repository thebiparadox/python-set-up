s = 'hipagbsabcdefg'

substring = ''
previousCharacter = ''
previousString = 0
longestString = ''

for count, i in enumerate(s):
    thisElement = ord(i)
    nextElement = ord(s[(count + 1) % len(s)])
    if thisElement <= nextElement:
        substring = substring + i
    else:
        if len(substring) > previousString:
            longestString = substring
        substring = ''
    previousCharacter = i

print('Longest substring in alphabetical order is', longestString)        
    
    





