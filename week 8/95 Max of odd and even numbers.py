'''
Write a code to receive integers (one integer at a time) until the user inputs either a zero or a
negative integer. While the program is receiving the input, it looks for the maximum of all odd numbers
and the maximum of all even numbers. You can rest assure that the given input contains at least one odd
and at least one even number. Finally, the program determines the difference between the two maximum
numbers.
Note: The value of each input is always less than 100,000.
Hint: Before determining the difference, the program should know which maximum number is
larger, so that the program returns the positive difference.
Input
Positive integers followed by the last negative integer.
Output
First line: The maximum value of all odd input integer
Second line: The maximum value of all even input integer
Third line: The difference of the two maximum values
'''

seq = set(map(int, input().split()[:-1]))
odd = set(num for num in seq if num % 2 == 1)
even = seq.difference(odd)


print(max(odd))
print(max(even))
print(abs(max(odd)-max(even)))

