import pandas as pd

coffee = pd.read_csv(r"C:\Users\saloni\Python_Lib\Pandas\Raw_data\coffee.csv")
print(coffee.head())

olympics_data = pd.read_excel(r"C:\Users\saloni\Python_Lib\Pandas\Raw_data\olympics-data.xlsx") # can also open specific sheets by , sheet_name="results"
print(olympics_data.head())


results = pd.read_parquet(r"C:\Users\saloni\Python_Lib\Pandas\Raw_data\results.parquet")
print(results.head())

bios = pd.read_csv(r"C:\Users\saloni\Python_Lib\Pandas\Raw_data\bios.csv")
