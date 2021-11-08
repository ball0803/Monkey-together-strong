d = dict()

# split given input
inputs = input().split()

# populate d with input
for i in range(0, len(inputs), 2):
    # if `i` is not in the dictionary 
    # create the `i` key with the value given
    # but if `i` is already a key in the dictionary
    # add the new value to the original
    if inputs[i] not in d:
        d[inputs[i]] = int(inputs[i+1])
    else:
        d[inputs[i]] += int(inputs[i+1])

print(d)
