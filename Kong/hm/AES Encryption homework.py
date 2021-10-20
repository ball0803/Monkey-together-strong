# # ============= fragment of code ===========
# # encryption inspired by AES (Advanced Encryption Standard)
# # Prabhas Chongstitvatana

def makeprintable(c):
    c1 = (c % 90) + 32 % 90
    return chr(c1)
    
# doxor xor ascii code of two characters c1, c2
def doxor(c1, c2):
    c3 = ord(c1) ^ ord(c2)
    c4 = makeprintable(c3)
    return c4

# xor key with text, keep it in printable range
def addkey(key, text):
    s = ''
    for a, b in zip(key, text):
        s += doxor(a, b)
    return s

# these two functions use "for", which we will learn later, just use
# it now
def createsubinput():
    s = ""
    for i in range(32,91):
        s += chr(i)
    return s

def createsuboutput():
    s = ""
    for i in range(33,91):
        s += chr(i)
    s += chr(32)
    return s

# findreplace use subinput and suboutput
def findreplace(char):  
    c1 = createsubinput().find(char)
    c2 = createsuboutput()[c1]
    return c2

# substitute characters in t with pattern in subinput and suboutput
def subbyte(t):
    s = ''
    for char in t:
        s += findreplace(char)
    return s

# rotate string one character to the right
def shiftonce(t):
    t1 = t[-1] + t[:-1]
    return t1

def shiftrow(t):
    t1 = shiftonce(t)
    t2 = shiftonce(t1)
    return t2

# coefficients use in multiply with fix polynomial in mixcolumn
# fixpoly = "2311 1231 1123 3112"
# we just hardcode it into the function
def mulc(c1, c2):
    c3 = ord(c1) * ord(c2)
    c4 = makeprintable(c3)
    return c4

def mixcolumn(t):
    seed = "2311123111233112"
    s = ''
    for a, b in zip(t, seed):
        s += mulc(a, b)
    return s

def oneround(key, text):
    t1 = addkey(key, text)
    t2 = subbyte(t1)
    t3 = shiftrow(t2)
    t4 = mixcolumn(t3)
    return t4

def encrypt(key, text):
    t1 = oneround(key, text)
    t2 = oneround(key, t1)
    return t2

def test(key, plaintext):
    print(key)
    txt1 = addkey(key, plaintext)
    print(txt1)
    txt2 = subbyte(txt1)
    print(txt2)
    txt3 = shiftrow(txt2)
    print(txt3)
    txt4 = mixcolumn(txt3)
    print(txt4)

    txt1 = addkey(key, txt4)
    print(txt1)
    txt2 = subbyte(txt1)
    print(txt2)
    txt3 = shiftrow(txt2)
    print(txt3)
    txt4 = mixcolumn(txt3)
    print(txt4)

def main():
    # key = input()
    # plaintext = input()
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)

if __name__ == '__main__':
    key = "ABCDEFGHIJKLMNOP"
    plaintext = "I LOVE PYTHON101"
    main()

    
#### End ######


