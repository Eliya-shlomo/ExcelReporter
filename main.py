import pandas as pd
import plotly.express as px 

# Load Excel data
df = pd.read_excel('sales_data.xlsx')

# Create Line chart
fig = px.line(df,x='Month',y='Sales',title='Monthly sales Overview')

# Export to HTML 
fig.write_html("sales_report.html")

print("✅ Report saved as sales_report.html")