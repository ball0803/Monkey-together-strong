'''
Write a program to read 5 floating numbers and display the maximum (max) and minimum (min) from the
received values as 2 decimal places, as show in the example below.
'''

nums = [float(input()) for _ in range(5)]
print(f'max {max(nums):.2f}')
print(f'min {min(nums):.2f}')
