# Series 

import pandas as pd

# list_1 = [1, 2, 3, 4, 5]
# # var = pd.Series(list_1)
# # print(pd.Series(list_1))
# # print(type(var))

# var_1 = pd.Series(list_1, index=['a', 'b', 'c', 'd', 'e'], dtype=float, name="Python")
# print(var_1)

# dict_1 = {"Name" : ['abc', 'def', 'ghi'], "Class" : [1, 3, 4], "Rank" : [23, 34, 45]}

# pds = pd.Series(dict_1)

# print(pds)
# print(type(pds))

# s = pd.Series(12)
# print(s)

# s_1 = pd.Series(12, index=['a', 'b', 'c', 'd'])
# print(s_1)


# list_2 = [2, 3, 4, 5, 6]

# var_2 = pd.DataFrame(list_2)

# print(var_2)
# print(type(var_2))

# dict_2 = {"Name" : ['abd', 'def', 'ghi'], "Class" : [2, 4, 6], "Rank" : [1, 3, 2]}

# var_3 = pd.DataFrame(dict_2)

# # print(var_3)

# # var_4 = pd.DataFrame(dict_2, columns=['Class', "Name"], index=['a', 'b', 'c'])
# # print(var_4)

# print(var_3['Name'][2])


# list_3 = [[2, 4, 6, 8], [1, 3, 5, 7]]
# var_3 = pd.DataFrame(list_3)

# print(var_3)

# sr = {"s":pd.Series([1, 2, 3]), "r":pd.Series([4, 5, 6])}
# var_6 = pd.DataFrame(sr)
# print(var_6)

# var = pd.DataFrame({"A":[1, 2, 3, 4], "B":[5, 6, 7, 8]})
# print(var)

# var["C"] = var["A"] + var["B"]

# print(var)

var = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8]})

var.insert(1, "C", var["A"])
var.insert(1, "D", [12, 13, 14, 15])

print(var)

# var["Python"] = var["A"][:2]

# print(var)

pop = var.pop("D")
print(pop)
print(var)