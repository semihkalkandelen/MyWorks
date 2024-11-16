"""
Perfect Number
a perfect number is a positive integer that is equal to the sum of its positive proper divisors, 
that is, divisors excluding the number itself.
"""

num = int(input("input the number and I will say if it is perfect number or not: "))
count = 1
for i in range(2,num):
    if num % i == 0:
        count = count + i
    else:
        pass
if count == num :
    print("number is perfect number")
    input("click any key to end")
else:
    print("number is not perfect number")
    input("click any key to end")