'''
Write a program to read two integers that are the date and month of birth. They are used to find the
user's zodiac sign. The program should print type the birth signs on the screen. The details of each zodiac
are as follows.
22 Dec - 19 Jan Capricorn
20 Jan - 18 Feb Aquarius
19 Feb - 20 Mar Pisces
21 Mar - 19 Apr Aries
20 Apr – 20 May Taurus
21 May – 21 Jun Gemini
22 Jun – 22 July Cancer
23 July – 22 Aug Leo
23 Aug – 22 Sep Virgo
23 Sep – 23 Oct Libra
24 Oct – 21 Nov Scorpio
22 Nov – 21 Dec Sagittarius
'''


d = int(input())
m = int(input())
if m == 1:
    print('Capricorn' if d < 20 else 'Aquarius')
elif m == 2:
    print('Aquarius' if d < 19 else 'Pisces')
elif m == 3:
    print('Pisces' if d < 21 else 'Aries')
elif m == 4:
    print('Aries' if d < 20 else 'Taurus')
elif m == 5:
    print('Taurus' if d < 21 else 'Gemini')
elif m == 6:
    print('Gemini' if d < 22 else 'Cancer')
elif m == 7:
    print('Cancer' if d < 23 else 'Leo')
elif m == 8:
    print('Leo' if d < 23 else 'Virgo')
elif m == 9:
    print('Virgo' if d < 23 else 'Libra')
elif m == 10:
    print('Libra' if d < 24 else 'Scorpio')
elif m == 11:
    print('Scorpio' if d < 22 else 'Sagittarius')
else:
    print('Sagittarius' if d < 22 else 'Capricorn')
