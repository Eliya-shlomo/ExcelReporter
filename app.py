from flask import Flask, send_file
import pandas as pd
import plotly.express as px
import pdfkit

app = Flask(__name__)

@app.route("/generate-report", methods=["GET"])
def generate_report():
    sheet_id = "1_VJj4-ciwH0FjxsyfNYaKPvd2b59YtP8zUhCf8C2-bU"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    df = pd.read_csv(url)

    line_chart = px.line(df, x='Month', y='Sales', title='📈 Monthly Sales')
    bar_chart = px.bar(df, x='Month', y='Sales', title='📊 Monthly Sales (Bar)')
    pie_chart = px.pie(df, names='Month', values='Sales', title='🥧 Sales Share')

    line_html = line_chart.to_html(full_html=False, include_plotlyjs='cdn')
    bar_html = bar_chart.to_html(full_html=False, include_plotlyjs=False)
    pie_html = pie_chart.to_html(full_html=False, include_plotlyjs=False)

    html_path = "report.html"
    pdf_path = "report.pdf"
    with open(html_path, "w", encoding="utf-8") as f:
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

    pdfkit.from_file(html_path, pdf_path)

    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
