#part 3 (1)
#
import pandas as pd
import seaborn as sns

# (3)
data=pd.read_csv("wdi_wide.csv")
b= data.info(
                     
# (4)
c= data.nunique()
print(c)

# (5)
d= data.describe()
print(d)

# this function gives different parameters such as count, mean, standard deviation etc of all the different columns in the dataset

# (6)


data["GNI per Capita"] = pd.DataFrame.round(data["GNI"] / data ["Population"])
f= data["GNI per Capita"]
print(f)
#e= pd.DataFrame.round(data["GNI per Capita"])                     

# (7) 
# a)

h= data["Region"]
g= data.value_counts() 