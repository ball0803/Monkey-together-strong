'''
The temperature of water indicates what state the water will be in at sea level.
Water will be in the solid state when the temperature is 0 °C (or 32 ° F). Water will vaporize (Gas) at 100
degrees Celsius (212 degrees Fahrenheit). If the temperature is between 0 - 100 degrees Celsius (32 - 212
degrees Fahrenheit), the water will be liquid.
Write a program to get the temperature and the unit of temperature (degrees of Celsius label with C or
degrees of Fahrenheit label with F) then shows what state of water will be in at that temperature.
'''

temp = float(input())
unit = input().lower()

true_temp = temp if unit == 'c' else (temp - 32) * (5 / 9)
if true_temp <= 0:
    print('solid')
elif true_temp >= 100:
    print('gas')
else:
    print('liquid')
