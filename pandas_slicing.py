"Create a Series of 10 elements and return the last 4 elements using slicing."

import pandas as pd

mylist = ["a","b","c","d","e","f","g","h","i","j"]

dataframe= pd.DataFrame(mylist)

dataframe = dataframe.iloc[-4:]

print(dataframe)