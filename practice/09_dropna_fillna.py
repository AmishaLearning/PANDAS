### Dropna & Fillna

import pandas as pd

csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\files\random_empty_data.csv")

print(csv_1)

# axis = 0 -- row
# print(csv_1.dropna())

# axis = 1 -- columns
# print(csv_1.dropna(axis = 1))


# how parameter

# print(csv_1.dropna(how = "any")) # removes all the rows where Nan is there

# print(csv_1.dropna(how = "all")) # removes only the row where every entry is NaN, rest if One or two are NaN then that will be visible

# fillna
# filling value at all places where NaN is present

# print(csv_1.fillna("PYTHON"))

# To fill data in particular column

# print(csv_1.fillna({"Age" : 100}))

# To fill value from previous row or forward row

# print(csv_1.fillna(method = "ffill")) # ForwardFill
# print(csv_1.fillna(method = "bfill")) # BackwardFill


# To fill data from previous/forward row(axis = 0/column(axis = 1)

# print(csv_1.fillna(method = "ffill", axis = 1))
