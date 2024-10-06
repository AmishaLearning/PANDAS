# Join 

import pandas as pd

var_1 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [15, 16, 17, 18]})
var_2 = pd.DataFrame({"C" : [10, 20, 30, 50], "D" : [11, 12, 13, 14]})

# print(var_1.join(var_2))

var_3 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [15, 16, 17, 18]}, index = ["a", "b", "c", "d"])
var_4 = pd.DataFrame({"C" : [10, 20], "D" : [11, 12]}, index = ["a", "b"])

# print(var_3.join(var_4))

print("LEFT")
print(var_4.join(var_3, how = "left"))

print("RIGHT")
print(var_4.join(var_3, how = "right"))

print("INNER")
print(var_4.join(var_3, how = "inner"))

# print("OUTER")
print(var_4.join(var_3, how = "outer"))


# var_5 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [15, 16, 17, 18]}, index = ["a", "b", "c", "d"])
# var_6 = pd.DataFrame({"C" : [10, 20], "B" : [11, 12]}, index = ["a", "b"])

# print(var_5.join(var_6, how = "outer", lsuffix = "_left", rsuffix="_right"))