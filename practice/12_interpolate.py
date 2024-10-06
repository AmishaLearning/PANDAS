import pandas as pd

# Assuming the file contains missing values (NaNs)
csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\files\interpolate.csv")

# Interpolating missing values in the DataFrame
print(csv_1.interpolate()) # works only for numerical data
