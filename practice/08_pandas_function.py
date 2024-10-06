# Functions in Pandas

import pandas as pd

# csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\sample_files\sample_data.csv")
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
# print(csv_1.index.array)

# change = csv_1["Name"][9] = "Amisha"
# print(change)
# print(csv_1)

# csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\files\random_file.csv")

# print(csv_1)

# .loc() : For Data of Particular Name

# new_csv = csv_1.loc[0, "Name"] = "AMisha"
# print(new_csv)

# print(csv_1.loc[:, ["Name", "City"]])


# For Data of Particular position

# print(csv_1.iloc[0, 0])

# # Drop a row or column

# print(csv_1)

# # Drop Column axis = 1 for column
# # print(csv_1.drop("Name", axis = 1))


# # Drop row axis = 0 for row
# print(csv_1.drop(1, axis=0))

## .loc() - labbel based and .iloc() - position based

csv_2 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\files\random_file.csv")

print(csv_2)

# loc_1 = csv_2.loc[0, "City"] = "AMisha"

# print(loc_1)
# print(csv_2)

iloc_1 = csv_2.iloc[0, 3] = "Aarushi"

print(iloc_1)

print(csv_2)
