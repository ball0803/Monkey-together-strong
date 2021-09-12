from string import ascii_lowercase

def swap_case(s: str):
    swapped = ''
    lower = set(char for char in ascii_lowercase)
    for char in s:
        if char in lower:
            swapped += char.upper()
        else:
            swapped += char.lower() if char.isalpha() else char
    return swapped
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    
    print(result)
    
