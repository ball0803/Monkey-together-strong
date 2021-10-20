string = input()

vowels = {'a', 'e', 'i', 'o', 'u'}

v = sum(1 for char in string if char.lower() in vowels)

print(v, len(string)-v)
