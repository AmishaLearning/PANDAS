# Group By - group the data according to the column name

import pandas as pd

var_1 = pd.DataFrame({"Name" : ["a", "b", "c", "d", "a", "b", "a", "b", "a", "c", "c", "d"], "S1" : [12, 23, 34, 45, 56, 67, 78, 89, 91, 99, 13, 88], "S2" : [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 67]})

# print(var_1)

var_new = var_1.groupby("Name")

# print(var_new)

# for x, y in var_new:
#     print(x)
#     print(y)
#     print()
    
# # I want only one groups data
# print(var_new.get_group("a"))

# # get minimum value
# print(var_new.min())

# # get maximum value
# print(var_new.max())

print(list(var_new))