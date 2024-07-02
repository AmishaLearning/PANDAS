# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.

import pandas as pd

# mydataset = {
#     'cars' : ['BMW', 'Volvo', 'Ford'],
#     'passings' : [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)
# print(pd.__version__)

# Series
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# nums = [1, 2, 3, 4, 5]
# nums_vars = pd.Series(nums)
# print(nums_vars)

# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.

# print(nums_vars[2])

# Create Labels
# With the index argument, you can name your own labels.

# numbers = [2, 4, 6, 8, 10]
# var_nums = pd.Series(numbers, index = ['a', 'b', 'c', 'd', 'e'])
# print(var_nums)
# print(var_nums['c'])

# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series
# Note: The keys of the dictionary become the labels.

# calories = {
#     'day1' : 420,
#     'day2' : 380,
#     'day3' : 390
# }

# var_calories = pd.Series(calories)
# print(var_calories)

# var_calories_1 = pd.Series(calories, index = ['day1', 'day2'])
# print(var_calories_1)

# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

# data = {
#     'calories' : [420, 380, 390],
#     'duration' : [50, 40, 45]
# }

# var_data = pd.DataFrame(data)
# print(var_data)

# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

# Locate Row
# As you can see from the result above, the DataFrame is like a table with rows and columns.
# Pandas use the loc attribute to return one or more specified row(s)

# print(var_data.loc[0])
# print(var_data.loc[[0, 1]])

# Named Index
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df) 
# print(df.loc['day2'])

# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).

# df = pd.read_csv('random_data.csv')
# print(df) 
# print(df.to_string()) - To print the entire DataFrame

# You can check your system's maximum rows with the pd.options.display.max_rows statement.
# print(pd.options.display.max_rows)

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# You can change the maximum rows number with the same statement.

# pd.options.display.max_rows = 9999
# df = pd.read_csv('data.csv')
# print(df) 

# Read JSON
# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
# df = pd.read_json('data.json')
# print(df.to_string()) 

# Load a Python Dictionary into a DataFrame:

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)

# print(df) 

# Viewing the Data
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# The head() method returns the headers and a specified number of rows, starting from the top.
# if the number of rows is not specified, the head() method will return the top 5 rows.

# df = pd.read_csv('data.csv')
# print(df.head(10))

# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.

df = pd.read_csv('data.csv')

# print(df.tail(5))

# Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.

# The info() method also tells us how many Non-Null values there are present in each column
# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data

print(df.info())
