#part 3 (1)
#
import pandas as pd
import seaborn as sns

data=pd.read_csv("wdi_wide.csv")
b=pd.info(data["Physicians","Population"])