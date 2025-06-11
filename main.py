import pandas as pd 

df = pd.read_excel('sales_data.xlsx', engine='openpyxl')
print(df)
