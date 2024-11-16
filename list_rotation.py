"""
Write a program that takes a list and rotates it by a specified number of positions to the right.
For example, given the list [1, 2, 3, 4, 5] and a rotation of 2, the result should be [4, 5, 1, 2, 3].
"""
givenlist = []
index = str(input("give me objects to put in a list: "))
index = index.split()
print("your list is",index)
rotation_number = int(input("enter the rotation number: "))
newlist = index[-rotation_number:] + index[:-rotation_number]
print(newlist,"is the new list")
input("click any key to end")

