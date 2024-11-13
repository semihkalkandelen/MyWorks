"""
Write a program that takes an integer input from the user and checks if the number is part of the Fibonacci sequence.
To check if a number n is Fibonacci, it must satisfy one of these two conditions:
5*n^2+4 or 5*n^2-4 must be a perfect square.
"""

number = int(input("Enter the number and I will check if it is in Fibonacci Series or not: "))
number1 = ((5*number**2-4)**(1/2))
number2 = ((5*number**2+4)**(1/2))
if number > 0:
    if number1 % 1 == 0  or number2 % 1 == 0:
        print("your number is in Fibonacci Series.") 
    else:
        print("your number is not in Fibonacci Series.")
else:
    print("enter a valid number.")