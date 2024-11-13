"""
Write a program that calculates the discount based on the total price entered by the user.
Use nested if-else statements to apply the following discount rules:
• If the price is greater than or equal to $500, apply a 20% discount.
• If the price is between $200 and $499, apply a 10% discount.
• If the price is less than $200, apply a 5% discount.
• If the price is negative, print an error message "Invalid price".
"""
price = float(input("Enter the price: "))
if price > 0:
    if price >= 500:
        price = price*4/5
    elif price >= 200:
        price = price*9/10
    elif price >= 0:
        price = price*95/100
    print("after the discount, new price is",price)
else:
    print("invalid price")