## .loc() - labbel based and .iloc() - position based

import pandas as pd

csv_2 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\files\random_file.csv")

print(csv_2)

# loc_1 = csv_2.loc[0, "City"] = "AMisha"

# print(loc_1)
# print(csv_2)

iloc_1 = csv_2.iloc[0, 3] = "Aarushi"

print(iloc_1)

print(csv_2)
