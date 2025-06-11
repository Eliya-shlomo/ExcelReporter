import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [1000, 1500, 1700, 1200]
}

df = pd.DataFrame(data)
df.to_excel('sales_data.xlsx', index=False)
