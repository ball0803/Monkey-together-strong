FORTUNE = {x:chr(x+65) for x in (i for i in range(10))}

number_plate = input()
numbers = list(map(int, *(char for char in number_plate.split())))
while sum(numbers) > 9:
    numbers = str(sum(numbers))
    numbers = list(map(int, *(char for char in numbers.split())))

print(FORTUNE[sum(numbers)])
