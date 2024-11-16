"""
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given 'n' scores. 
Store them in a list and find the score of the runner-up.
"""

mylist = []
count = 1
print("Enter the scores. for end the sequence press 'x' ")
while True:
    scores = input(f"Score {count} is: ")
    if scores.isnumeric() == True:
        mylist.append(scores)
        count += 1
    elif scores == "x":
        if len(mylist) == 1:
            value = mylist.pop()
            print(f"you enter only one number and it is: {value}")
            input("click any key to end")
            break
        elif len(mylist) == 0:
            print("you did not enter any number.")
            continue
        else:
            mylist=sorted(mylist)
            print("second highest value you entered is: ", mylist[-2])
            input("click any key to end")
        break
    else:
        print("please enter a valid value (x or a score)")