# filters

import pandas as pd

df_1 = pd.DataFrame({"A" : [2, 3, 4, 5], "B" : [6, 7, 8, 9]})

print(df_1)

df_1["C"] = df_1["A"] + df_1["B"]

df_1["D"] = df_1["A"] >= 5

print(df_1)