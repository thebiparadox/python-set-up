string = input('Enter a string: ') #gets string from the user

numberOfVowels = 0 #vowel counter

for letter in string: #iterates over characters in the string and counts vowels
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        numberOfVowels = numberOfVowels + 1
print('Number of vowels:', numberOfVowels) #prints number of vowels in string