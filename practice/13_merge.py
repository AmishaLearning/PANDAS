# MERGE

# While merging two dataframes, the column names should be same.
# .merge(dataframe_1, dataframe_2, on="common column name")

import pandas as pd

var_1 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8]})
var_2 = pd.DataFrame({"A" : [1, 2, 3, 4], "C" : [13, 14, 15, 16]})

# The column names should be same and also the data should be same, otherwise it will only give the common values

# print(pd.merge(var_1, var_2, on="A"))

var_3 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8]})
var_4 = pd.DataFrame({"A" : [1, 2, 3, 5], "C" : [13, 14, 15, 16]})

# print(pd.merge(var_3, var_4, on="A"))

# how : "inner", "left", "right", "outer", "cross" - default is "inner"

# print("INNER") # default
# print(pd.merge(var_3, var_4, on="A", how="inner"))

# print("LEFT") # var_3 is left, var_4 is right - works according to var_3 values
# print(pd.merge(var_3, var_4, on="A", how="left"))

# print("RIGHT") # var_3 is right, var_4 is left - works according to var_4 values
# print(pd.merge(var_3, var_4, on="A", how="right"))

# print("OUTER")
# print(pd.merge(var_3, var_4, on="A", how="outer"))

# # To see what data is present 
# print("INDICATOR")
# print(pd.merge(var_3, var_4, on="A", how="outer", indicator=True))

var_5 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8]})
var_6 = pd.DataFrame({"A" : [1, 2, 3, 5], "B" : [13, 14, 15, 16]})

print(pd.merge(var_5, var_6))

print("LEFT INDEX & RIGHT INDEX")
print(pd.merge(var_5, var_6, left_index=True, right_index=True))

print("SUFFIX") # change the suffix name of the columns
print(pd.merge(var_5, var_6, left_index=True, right_index=True, suffixes=("_left", "_right")))

# Merge : adds two dataframes on the basis of common column name