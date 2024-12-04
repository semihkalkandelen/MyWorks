"""
Stuttering Function
Write a function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis ... 
and space after each, and then the word is pronounced with a question mark ?.
"""

sentence = input("i...i.. input the word pweaseee?").split()
mylist = list(sentence)
for i in mylist:
    print(mylist[0:2],"...",mylist[0:2],"...",sentence,"?",end="")