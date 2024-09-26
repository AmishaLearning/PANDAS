# Data Frames 

import pandas as pd

# List

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8]

# dataframe_1 = pd.DataFrame(list_1)
# print(dataframe_1)
# print(type(dataframe_1))

# Dictionary
# The value in the dictionary should be of same length.

# dict_1 = {"a" : [1, 2, 3, 4], "b" : [5, 6, 7, 8], "c" : [9, 10, 11, 12], 1 : [13, 14, 15, 16]}

# dataframe_2 = pd.DataFrame(dict_1)
# print(dataframe_2)
# print(type(dataframe_2))

# # Print a specific column

# dataframe_3 = pd.DataFrame(dict_1, columns=["a", 1], index=["a", "b", "c", "d"])
# print(dataframe_3)
# print(type(dataframe_3))

# Get value of a particular index 

# dict_2 = {"a": [1, 2, 3, 4], "b": [5, 6, 7, 8], "c": [9, 10, 11, 12], 1: [13, 14, 15, 16]}

# dataframe_4 = pd.DataFrame(dict_2)

# print(dataframe_4)
# print(dataframe_4["c"][2])

# Dataframe from list of list

# list_2 = [[1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17]]

# dataframe_5 = pd.DataFrame(list_2, columns=["a", "b", "c", "d", "e", "f"])

# print(dataframe_5)

# Dataframe using series

series_1 = {"a": pd.Series([1, 2, 3, 4]), "b": pd.Series([5, 6, 7, 8]), "c": pd.Series([9, 10, 11, 12])}

dataframe_6 = pd.DataFrame(series_1)
print(dataframe_6)