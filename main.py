import pandas as pd
import plotly.express as px 

# Load Excel data
df = pd.read_excel('sales_data.xlsx')

# Create Line chart
line_chart = px.line(df, x='Month', y='Sales', title='📈 Line Chart – Monthly Sales')
bar_chart = px.bar(df, x='Month', y='Sales', title='📊 Bar Chart – Monthly Sales')
pie_chart = px.pie(df, names='Month', values='Sales', title='🥧 Pie Chart – Sales Share')

line_html = line_chart.to_html(full_html=False, include_plotlyjs='cdn')
bar_html = bar_chart.to_html(full_html=False, include_plotlyjs=False)
pie_html = pie_chart.to_html(full_html=False, include_plotlyjs=False)

with open("full_sales_report.html", "w", encoding="utf-8") as f:
    f.write(f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Sales Report</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <h1>📊 Sales Report</h1>
        <h2>1. Line Chart</h2>
        {line_html}
        <h2>2. Bar Chart</h2>
        {bar_html}
        <h2>3. Pie Chart</h2>
        {pie_html}
    </body>
    </html>
    """)
print("✅ full_sales_report.html was generated successfully.")
