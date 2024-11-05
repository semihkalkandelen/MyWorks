
"""
Leap Day Problem

In the Gregorian calendar, three conditions are used to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
"""
year = int(input("Tell me the year so I will say if it is leap year or not: "))
if year % 400 == 0:
    print("This year is a leap year.")
else:
    if year % 4 == 0 and year % 100 !=0:
        print("This is a leap year.")
    else:
        print("This is not a leap year.")