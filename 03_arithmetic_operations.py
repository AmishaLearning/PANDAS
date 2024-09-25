# Arithmetic operations 

import pandas as pd

# dataframe_1 = pd.DataFrame({"A":[1, 2, 3, 4, 5], "B":[6, 7, 8, 9, 10]})
# print("Original Dataframe")
# print(dataframe_1)

# dataframe_1["C"] = dataframe_1["B"] - dataframe_1["A"]
# print("Subtraction")
# print(dataframe_1[["A", "B", "C"]])

# dataframe_1["D"] = dataframe_1["B"] + dataframe_1["A"]
# print("Addition")
# print(dataframe_1[["A", "B", "D"]])

# dataframe_1["E"] = dataframe_1["B"] * dataframe_1["A"]
# print("Multiplication")
# print(dataframe_1[["A", "B", "E"]])

# dataframe_1["F"] = dataframe_1["B"] / dataframe_1["A"]
# print("Division")
# print(dataframe_1[['A', 'B', 'F']])

# Greater than, Less than, Equal to

dataframe_2 = pd.DataFrame({"A":[10, 20, 30, 40], "B":[15, 16, 17, 18]})

dataframe_2["PythonA"] = dataframe_2["A"] <= 20
dataframe_2["PythonB"] = dataframe_2["B"] <= 17
print(dataframe_2)
