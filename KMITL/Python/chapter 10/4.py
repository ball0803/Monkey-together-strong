d = dict()

# split given input
inputs = input().split()

# iterate through every other item in `inputs`
# using the ith index as key 
# and i+1th index as value
for i in range(0, len(inputs), 2):
    d[inputs[i]] = inputs[i+1]

print(d)
