# Series Data Structure : 1D array

import pandas as pd

list_1 = [1,2,3,4,5]
series_1 = pd.Series(list_1)

print(series_1)
print(type(series_1))

# print(series_1[4])

# Series with custom index

# list_2 = [4, 5, 6, 7, 8]
# series_2 = pd.Series(list_2, index=['a', 'b', 'c', 'd', 'e'])

# print(series_2)

# Changge Data type of Series

# list_3 = [2, 4, 6, 8]
# series_3 = pd.Series(list_3, index=['a', 'b', 'c', 'd'], dtype="float")

# print(series_3)

# name attribute

# list_4 = [4, 5, 6, 7]
# series_4 = pd.Series(list_4, index=['a', 'b', 'c', 'd'], name="Python")

# print(series_4)

# Dictionary to Series 
# Whenever we use mixed data the data type of the series will be object.

# dict_1 = {"Name" : ["Python", "Java", "C++", "Ruby"], "Popularity" : [100, 90, 80, 70], "Rank" : [1, 2, 3, 4]}

# series_1 = pd.Series(dict_1)

# print(series_1)

# Series for Single Value

# series_2 = pd.Series(5)

# print(series_2)
# print(type(series_2))

# If you want to get multiple series for single value.

# series_3 = pd.Series(5, index=['a', 'b', 'c', 'd', 'e'])
# print(series_3)

# Adding two series
# If the index is not matching then it will return NaN, but in numpy it will return an Broadcasting error.

# series_1 = pd.Series(12, index=[1, 2, 3, 4, 5, 6, 7, 8])
# series_2 = pd.Series(12, index=[1, 2, 3, 4])

# print(series_1 + series_2)

