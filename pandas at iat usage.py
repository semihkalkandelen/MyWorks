"Write code to access a specific cell in the DataFrame using .at[] and .iat[]."

import pandas as pd
mydict = {"name":["ahmet","hamdi","aslı"],
          "maaş":[10,100,1000]
          }

dataframe = pd.DataFrame(mydict,index=[1,2,3])

asli_maas = dataframe.at[3,"maaş"]

print(asli_maas)

iat  = dataframe.iat[2,1]
print(iat)

"""
or

dataframe = dataframe.set_index('name')
asli_maas = dataframe.at("asli","maaş")
print(asli_maas)


"""