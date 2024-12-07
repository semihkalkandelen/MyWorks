word = input("enter the words and I will count the amount of letters ")
dictionary = {letter: word.count(letter) for letter in word}
dictionary.pop(" ", None)
print(dictionary)
