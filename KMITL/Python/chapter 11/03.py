WORDS = tuple("Fusce vehicula mattis eleifend condimentum nisl sit amet magna semper pharetra Proin aliquet magna non dapibus blandit Quisque nibh".split())
word = input()
try:
    print("\n")
    print(f"{word} {WORDS.index(word)}")
except ValueError:
    print(f"Word \"{word}\" is not in tuple")
