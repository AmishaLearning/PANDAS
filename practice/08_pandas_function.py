# Functions in Pandas

import pandas as pd

csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\sample_files\sample_data.csv")
# print(csv_1)

# # To get index
# print(csv_1.index)

# # To get columns
# print(csv_1.columns)

# # To get mean, median, std - only for numerical data
# print(csv_1.describe())

# # To get starting 5 rows from above
# print(csv_1.head())

# print(csv_1.head(2))

# # To get last 5 rows
# print(csv_1.tail())
# print(csv_1.tail(2))

# # To get specific column data
# print(csv_1["Name"])

# TO get specific row data
# print(csv_1[:4:2])
# print(csv_1[:3])

# print(type(csv_1))

# To show index in array
print(csv_1.index.array)