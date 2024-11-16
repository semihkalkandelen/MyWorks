"""
Collatz conjecture
in the 3x+1 problem, no matter what number you start with, you will always eventually reach 1.
"""

num = int(input("enter the number and I will show you how it is going to reach 1: "))
while True:
    if num == 1:
        input("click any key to end")
        break
    elif num % 2 == 0:
        print(f"{num} is even\n{num}/2 = ", int(num/2))
        num = int(num/2)
    else:
        print(f"{num} is odd\n{num}*3+1 = ", int(num*3+1))
        num = int(num*3+1)