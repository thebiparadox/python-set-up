s = 'abccdef'

substring = ''
previousCharacter = ''
numberInString = 0
longestString = ''

for i in s:
    if ord(s[0]) == ord(s[1]) - 1:
        substring = substring + i
    else:
        if len(substring) > numberInString:
            longestString = substring
        substring = ''
    previousCharacter = i

print('Longest substring in alphabetical order is', longestString)        
    
    





