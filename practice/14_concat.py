# Concate - Series

# Concate - merge dataframes, no need of common column name

import pandas as pd

# sr_1 = pd.Series([1, 2, 3, 4, 5])
# sr_2 = pd.Series([11, 12, 13, 14, 15])

# # print(sr_1)
# # print(sr_2)

# print(pd.concat([sr_1, sr_2]))

# Concate - DataFrame

var_1 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8]})
var_2 = pd.DataFrame({"A" : [1, 2, 3, 5], "B" : [13, 14, 15, 16]})

# axis = 0 --merges along the rows - default
print(pd.concat([var_1, var_2]))

# axis = 1 --merges along the columns
print(pd.concat([var_1, var_2], axis=1))

var_3 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8]})
var_4 = pd.DataFrame({"A" : [1, 2, 3, 5], "C" : [13, 14, 15, 16]})

print(pd.concat([var_3, var_4], axis=1))

# outer - union (default), inner - intersection
import pandas as pd

# var_3 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8]})
# var_4 = pd.DataFrame({"A" : [1, 2], "C" : [13, 14]})

# print("OUTER")
# print(pd.concat([var_3, var_4], axis = 1, join = "outer"))

# print("INNER")
# print(pd.concat([var_3, var_4], axis = 1, join = "inner"))

# var_3 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8]})
# var_4 = pd.DataFrame({"A" : [1, 2, 3, 4], "C" : [13, 14, 15, 16]})

# print("KEY")
# print(pd.concat([var_3, var_4], keys = ["D1", "D2"], axis = 1))
