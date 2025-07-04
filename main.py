import pandas as pd
import plotly.express as px
import pdfkit


# Load data from Google Sheets
sheet_id = "1_VJj4-ciwH0FjxsyfNYaKPvd2b59YtP8zUhCf8C2-bU"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
df = pd.read_csv(url)

# Create Charts
line_chart = px.line(df, x='Month', y='Sales', title='📈 Line Chart – Monthly Sales')
bar_chart = px.bar(df, x='Month', y='Sales', title='📊 Bar Chart – Monthly Sales')
pie_chart = px.pie(df, names='Month', values='Sales', title='🥧 Pie Chart – Sales Share')

# Convert charts to HTML fragments
line_html = line_chart.to_html(full_html=False, include_plotlyjs='cdn')
bar_html = bar_chart.to_html(full_html=False, include_plotlyjs=False)
pie_html = pie_chart.to_html(full_html=False, include_plotlyjs=False)

# Write full HTML report
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

pdfkit.from_file("full_sales_report.html", "sales_report.pdf")
print("✅ sales_report.pdf was generated successfully.")