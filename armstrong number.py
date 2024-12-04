enterednum = input("enter a number and I will tell whether it is an armstrong number or not.")
lenght = len(enterednum)
sum = 0
for number in enterednum:
    number = int(number)
    sum += number**lenght
if int(enterednum) == sum:
    print(f"{enterednum} is an armstrong number.")
else:
    print(f"{enterednum} is not an armstrong number.")