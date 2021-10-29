'''
Write a program to enter the name of each card as the full name according to the symbol of the cards
received. The symbols are called as follows
The card labeled by numbers 2 - 10, you can call according to the value of the cards as numbers 2 – 10.
The card labeled by A is Ace, J is Jack, Q is Queen, and K is King.
The group of cards are divided into 4 symbols: D is diamonds, H is hearts, S is Spades, and C is Clubs.
The card names are called from card points followed by the word “of” and followed by a group of cards,
for example QS is called Queen of Spades.
'''

card = input()
pref, suff = card[:-1].lower(), card[-1].lower()

if pref == 'k':
    pref = 'King'
elif pref == 'q':
    pref = 'Queen'
elif pref == 'j':
    pref = 'Jack'
else:
    pref = 'Ace'

if suff == 'c':
    suff = 'Clubs'
elif suff == 'h':
    suff = 'Hearts'
elif suff == 's':
    suff = 'Spades'
else:
    suff = 'Diamonds'

print(f'{pref} of {suff}')
