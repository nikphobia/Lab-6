#part 3 
# (1)

#1. The amount of countries with no physicians
#2. The life expectancies associated to which country
#3. The average tertiary education for women

import pandas as pd
import seaborn as sns

# (2)
data=pd.read_csv("wdi_wide.csv")

print ("3.___________________________________________________")
# (3)
info= data.info()
print ("4.___________________________________________________")
# (4)
unique= data.nunique()
print(unique)

print ("5.___________________________________________________")

# (5)
describe = data.describe()
print(describe)

print ("6.___________________________________________________")

# (6)
data["GNI per Capita"] = pd.DataFrame.round(data["GNI"] / data ["Population"])
GNI_Cap= data["GNI per Capita"]
print(GNI_Cap)

print ("7.___________________________________________________")

# (7)
#a

value_region = pd.DataFrame(data["Region"].value_counts())

print(value_region)
#b

value_eco = pd.DataFrame(data["High Income Economy"].value_counts())
print(value_eco)

print ("8.___________________________________________________")

# (8)
df = pd.DataFrame(data)
cross= pd.crosstab(df['High Income Economy'], df['Region'])
print(cross)

print ("9.___________________________________________________")

#(9)
number=0
n=1
for i in df["Life expectancy, female"]:
    if i > 80:
        print(df["Country Name"][n],"life expectancy:", i)
        n += 1
        number +=1
print ("number of countries: ", number)