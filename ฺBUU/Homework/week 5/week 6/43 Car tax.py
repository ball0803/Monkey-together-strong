'''
In calculating the vehicle tax, the car model (which year was it built in A.D.) and the engine CC (Bigger
engines pay more taxes.) Given the car tax schedule as follows,
Car model in A.D.                           Engine cc.                              Tax
A.D. 1900 or older                          1500 cc. or older                       1250
                                            
                                            More than 1500 cc. but not              1400
                                            more than 2000 cc.
                                            
                                            More than 2000 cc.                      2000

A.D. 1991-1999                              1500 cc. or older                       1100
                                            
                                            More than 1500 cc. but not              1300
                                            more than 2000 cc.
                                            
                                            More than 2000 cc.                      1700

From A.D. 2000 onwards                      Not more than 1500 cc.                  1000

                                            More than 1500 cc. but not              1200
                                            more than 2000 cc.  

                                            More than 2000 cc.                      1500

Write a program to get the year of the car in A.D. and size of the engine. Then print out the car tax price to
be paid on the screen.
'''

year = int(input())
size = int(input())

if year <= 1990:
    if size <= 1500:
        print(1100)
    elif 1500 < size <= 2000:
        print(1300)
    else:
        print(1700)
elif 1990 < year <= 1999:
    if size <= 1500:
        print(1250)
    elif 1500 < size <= 2000:
        print(1400)
    else:
        print(2000)
else:
    if size <= 1500:
        print(1000)
    elif 1500 < size <= 2000:
        print(1200)
    else:
        print(1500)
