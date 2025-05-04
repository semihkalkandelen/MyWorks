def calculate_discount(price , percentage , member = False):
    total = price * (100 - percentage)* 100
    if member == True:
        total = 90*total/100
    return total

print(calculate_discount(100,20,True))