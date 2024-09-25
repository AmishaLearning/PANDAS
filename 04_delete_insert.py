# Delete and Insert

# .insert(index numner, column name, value)

import pandas as pd

# dataframe_1 = pd.DataFrame({"A":[1, 2, 3, 4, 5], "B":[6, 7, 8, 9, 10]})
# # dataframe_1.insert(1, "C", [11, 12, 13, 14, 15])

# # To make duplicate column
# dataframe_1.insert(1, "Python", dataframe_1["A"])
# dataframe_1.insert(1, "Java", [11, 12, 13, 14, 15])
# print(dataframe_1)

# Adding a specified number of values 

# dataframe_2 = pd.DataFrame({"A":[1, 2, 3, 4], "B":[5, 6, 7, 8]})

# dataframe_2["New Column"] = dataframe_2["A"][:2]

# print(dataframe_2)

# Delete a column - pop()

dataframe_3 = pd.DataFrame({"A":[1, 2, 3, 4], "B":[5, 6, 7, 8], "C":[9, 10, 11, 12]})

popped = dataframe_3.pop("A")

print(popped)
print(dataframe_3)

del dataframe_3["B"]

print(dataframe_3)