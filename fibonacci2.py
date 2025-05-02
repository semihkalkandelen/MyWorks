def fibonacci(num):    
    mylist = [0]
    base0 = 0
    base1 = 1
    count = 0
    while num-1 > count:
            temp = base1 + base0
            mylist.append(temp)
            base1 = base0
            base0 = temp
            count += 1
    return mylist

print(fibonacci(20))




