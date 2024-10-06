# Append : unlike join, if column value is same then also the dataframes will be appended

import pandas as pd

var_1 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [15, 16, 17, 18]}, index = ["a", "b", "c", "d"])
var_2 = pd.DataFrame({"C" : [10, 20], "B" : [11, 12]}, index = ["a", "b"])

var_1.append(var_2)

# print(var_1)

## No Longer being used in Pandas - alternate is pd.concate()