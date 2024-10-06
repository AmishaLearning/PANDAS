# Apply : It is used to apply the functionality to eac and every element either column or row wise
import pandas as pd

csv_1 = pd.read_csv(r"C:\Users\Misha\Desktop\Coding\GIT HUB\PANDAS\04-10-24\files\random_file.csv")

print(csv_1)

# apply() 

print(csv_1.apply(len))

# shows len for each row
print(csv_1.apply(len, axis = 1))