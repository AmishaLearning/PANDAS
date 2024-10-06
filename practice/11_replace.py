import pandas as pd

csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\files\random_file.csv")

print(csv_1)

# print(csv_1.replace(to_replace = "Teacher", value = "Monitor"))

# print(csv_1.replace([3, 12, 6], 100))
# print(csv_1.replace(["Teacher", "Engineer"], "Monitor"))

# Regex 

# print(csv_1.replace("[A-Za-z]", "AMISHA", regex = True))

# Dictionary
# print(csv_1.replace({"Name" : "Bob"}, "TOM"))

# Replace with backward or forward data

# print(csv_1.replace("Teacher", method = "ffill"))

# set limit to change limited amount of data

# print(csv_1.replace("Teacher", method = "ffill", limit = 2))

# inplace = True - to change the original data no copy will be created
print(csv_1.replace("Teacher", method = "ffill", inplace = True))