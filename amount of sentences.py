sentence = input("give me a sentence and I will say how long is the sentence by each word. ").split()
dictionary = {word: len(word) for word in sentence}
print(dictionary)