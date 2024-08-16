
import pandas as pd

# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

# Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.

# df = pd.read_csv('workout_data.csv')
# new_df = df.dropna()
# print(new_df.to_string())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# If you want to change the original DataFrame, use the inplace = True argument:

# df.dropna(inplace = True)
# print(df.to_string())

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:

# df = pd.read_csv('workout_data.csv')

# df.fillna(130, inplace = True)
# print(df.to_string())

# Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.
# To only replace empty values for one column, specify the column name for the DataFrame:

# df = pd.read_csv('workout_data.csv')
# df["Calories"].fillna(130, inplace = True)
# print(df.to_string())

# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# df = pd.read_csv('workout_data.csv')

# x = df["Calories"].mean()

# df["Calories"].fillna(x, inplace = True)
# print(df.to_string())

# Data of Wrong Format
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

# df = pd.read_csv('workout_data.csv')

# df['Date'] = pd.to_datetime(df['Date'])

# print(df.to_string())

# Removing Rows
# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.

df = pd.read_csv('workout_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())