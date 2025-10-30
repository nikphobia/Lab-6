#part 4

import pandas as pd
import seaborn as sns

# 1

data = pd.read_csv("wdi_wide.csv")
data["GNI per Capita"] = pd.DataFrame.round(data["GNI"]/data["Population"])

#plot-male

sns.relplot(
    data = data,
    x = "GNI per Capita",
    y = "Life expectancy, male",
    kind = "scatter"
)

#plot-female

sns.relplot(
    data = data,
    x = "GNI per Capita",
    y = "Life expectancy, female",
    kind = "scatter"
)


# 2

#plot-male

sns.relplot(
    data = data,
    x = "GNI per Capita",
    y = "Life expectancy, male",
    hue = "Region",
    kind = "scatter"
)

#plot-female

sns.relplot(
    data = data,
    x = "GNI per Capita",
    y = "Life expectancy, female",
    hue = "Region",
    kind = "scatter"
)

# 3

#plot-male

sns.relplot(
    data = data,
    x = "GNI per Capita",
    y = "Life expectancy, male",
    hue = "Region",
    kind = "line",
    ci = "sd",
)

#plot-female

sns.relplot(
    data = data,
    x = "GNI per Capita",
    y = "Life expectancy, female",
    hue = "Region",
    kind = "line",
    ci = "sd",
)

# 4

#plot-male

sns.lmplot(
    data = data,
    x = "GNI per Capita",
    y = "Life expectancy, male",
    hue = "Region"
    )

#plot-female

sns.lmplot(
    data = data,
    x = "GNI per Capita",
    y = "Life expectancy, female",
    hue = "Region"
)