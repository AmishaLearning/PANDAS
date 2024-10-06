import pandas as pd

# dict_1 = pd.DataFrame({"A" : [1, 2, 3, 4, 5, 6], "B" : [1, 2, 3, 4, 5, 6], "C" : [1, 2, 3, 4, 5, 6]})

# print(dict_1)

# # dict_1.to_csv("Test_02.csv")
# # dict_1.to_csv("Test_02_1.csv", index=False)

# dict_1.to_csv("Test_02_2.csv",index = False, header=['a', 'b', 'c'])

# csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\test_file.csv")

# csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\test_file.csv", nrows=1, usecols=["Column1"])

# csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\test_file.csv", skiprows=1)

# csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\test_file.csv", index_col="Column1")

# csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\test_file.csv", names=["AA", "BB", "CC"])

# print(csv_1)