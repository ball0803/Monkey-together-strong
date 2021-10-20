arr = input().split()

if any(len(word) < 2 for word in arr):
    print('Input Error')
else:
    for word in arr:
        for i in range(len(word)):
            l = i
            r = (i - (i * 2)) - 1
            if word[l] != word[r]:
                print(f'{word} is not a palindrome')
                break
        else:
            print(f'{word} is a palindrome')

