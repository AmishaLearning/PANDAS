# Excel(Table) & CSV(comma separated values) Files

# Write CSV file

import pandas as pd

dict_1 = {"a" : [1, 2, 3, 4, 5, 6], "b" : [1, 2, 3, 4, 5, 6], "c" : [1, 2, 3, 4, 5, 6]}

dataframe_1 = pd.DataFrame(dict_1)
# print(dataframe_1)

# dataframe_1.to_csv("Test_new.csv")
# dataframe_1.to_csv("Test_new_1.csv", index=False)

dataframe_1.to_csv("Test_new_2.csv", index=False, header=["A", "B", "C"])
