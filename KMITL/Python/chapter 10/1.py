frequency = dict()

# split given input
inputs = input().split()

# populate frequency with input
for i in inputs:
    # if `i` is not in the dictionary 
    # create the `i` key with the value of 1
    # but if `i` is already a key in the dictionary
    # add 1 to the value
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency[i] += 1

# search for the key with the `maximum` value
# breaking out when found
for key, val in frequency.items():
    if val == max(frequency.values()):
        print(f'Max = {key} => {val}')
        break
