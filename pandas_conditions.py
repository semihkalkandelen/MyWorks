"Given a Series of student grades, retrieve all grades greater than 80 using a condition."
import pandas as pd

mydict = {"name":["ali","ahmet","mehmet","selami"],
          "grades": [10,90,75,95]
          }

dataframe = pd.DataFrame(mydict)

answer = dataframe[dataframe["grades"]>80]

print(answer)