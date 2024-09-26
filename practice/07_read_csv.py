# Read CSV

import pandas as pd

# csv_1 = pd.read_csv("sample_data.csv")

# for getting desired number of rows
# csv_1 = pd.read_csv("sample_data.csv", nrows=3)

# for getting desired columns
# csv_1 = pd.read_csv("sample_data.csv", usecols=["Name", "Age"])
# csv_1 = pd.read_csv("sample_data.csv", usecols=[0, 1])

# print(csv_1)

# Skip rows
# csv_1 = pd.read_csv("sample_data.csv", skiprows=[0])

# Make column as Index
# csv_1 = pd.read_csv("sample_data.csv", index_col="Name")

# Make a row as header
# csv_1 = pd.read_csv("sample_data.csv", header=2)

# Change column names/ heading
# csv_1 = pd.read_csv("sample_data.csv", names=["A", "B", "C", "D"])

# print(csv_1)
# print(type(csv_1))


# If csv has no heading, the code will make the first row as heading

csv_2 = pd.read_csv("sample_data.csv", dtype={"Age": float})

print(csv_2)