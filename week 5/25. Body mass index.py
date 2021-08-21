'''
Body mass index is a measure to assess body fat. It is widely use because it is easy to calculate and can
apply to everyone. The Body Mass Index (BMI) can calculate using the following equation.
Body Mass Index (BMI) = weight / height2 (Height in meters)
If BMI is 40 or greater, the program should print Fattest.
If BMI is 35.0 or above but less than 40 , the program should print Fat level II.
If BMI is 28.5 or above, but less than 35, the program should print Fat level I.
If BMI is 23.5 or above but less than 28.5, the program should print Overweight.
If BMI is 18.5 or above but less than 23.5, the program should print Normally.
If BMI is less than 18.5, the program should print Underweight.
Input
The first line is height (cm)
The second line is weight (kg)
Output
The first line shows BMI (2 decimal places).
The second line shows the interpretation of BMI level.
'''

h = float(input()) / 100
w = float(input())

bmi = w / (h * h)
print(f'{bmi:.2f}')

if bmi >= 40:
    print('Fattest')
elif 40 > bmi >= 35:
    print('Fat level II')
elif 35 > bmi >= 28.5:
    print('Fat level I')
elif 28.5 > bmi >= 23.5:
    print('Overweight')
elif 23.5 > bmi >= 18.5:
    print('Normally')
else:
    print('Underweight')
