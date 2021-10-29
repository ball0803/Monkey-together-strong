'''
Write a code that repeatedly receives lowercase English letters (one letter at a time) until the
letter q is found. (If the user inputs the letter q, the program stops receiving data and outputs the
following:
1. All the letters input by the user, but in the form of the capital letters.
2. The total number of the vowel letters (a, e, i, o, or u) input by the user.
'''

ans = []
vowels = {char for char in 'AEIOU'}
vowels_count= 0
while True:
    char = input().upper()
    if char == 'Q':
        break  
    else:
        vowels_count += 1 if char in vowels else 0
        ans.append(char)

print(*ans, vowels_count, sep='\n')
