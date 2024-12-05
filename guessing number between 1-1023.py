print("think any number between 1-1023 and I will try to guess it with maximum 10 try.")
guessing_number1 = 512
guessing_number2 = 256
variable = 2048
count = 1 
while variable % 2 == 0 :
    if count ==11:
        print("you lied to me at least one of your responses. please restart the program again.")
        variable -= 1
        a = input("press any key to exit.")
    else:    
        guess = input(f"is your number {guessing_number1}? y/n: ")
        if guessing_number1 == 1 or guessing_number1 == 1023:
                print("your number is either lowest (1) or highest (1023) number")
                variable -=1
                a = input("press any key to exit.")
        elif guess == "y":
            print(f"your number is {guessing_number1} and I found it with {count} guess(es).")
            variable -= 1
            a = input("press any key to exit.")
        elif guess == "n":
            print(f"guess count: {count}")
            answer = input(f"is the number higher than {guessing_number1}? y/n: ")
            if answer == "y": 
                guessing_number1 += guessing_number2
                guessing_number2 /= 2
                variable /= 2
                count +=1
            elif answer == "n":
                guessing_number1 -= guessing_number2
                guessing_number2 /= 2 
                variable /= 2
                count += 1
            else:
                print("enter a valid key 'y' or 'n'")
        else:
            print("enter a valid key 'y' or 'n'")