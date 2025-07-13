import pandas as pd
from fpdf import FPDF

# Load the CSV data
data = pd.read_csv('data.csv')

# Calculate summary
average_score = data['Score'].mean()
highest_score = data['Score'].max()
lowest_score = data['Score'].min()
topper = data.loc[data['Score'].idxmax(), 'Name']

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# Title
pdf.cell(200, 10, txt="Automated Report - Student Scores", ln=True, align='C')
pdf.ln(10)

# Table Header
pdf.set_font("Arial", 'B', 12)
pdf.cell(80, 10, "Name", 1)
pdf.cell(40, 10, "Score", 1)
pdf.ln()

# Table Data
pdf.set_font("Arial", '', 12)
for index, row in data.iterrows():
    pdf.cell(80, 10, row['Name'], 1)
    pdf.cell(40, 10, str(row['Score']), 1)
    pdf.ln()

pdf.ln(10)

# Summary Section
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Summary", ln=True)

pdf.set_font("Arial", '', 12)
pdf.cell(200, 10, txt=f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Highest Score: {highest_score}", ln=True)
pdf.cell(200, 10, txt=f"Lowest Score: {lowest_score}", ln=True)
pdf.cell(200, 10, txt=f"Topper: {topper}", ln=True)

# Save PDF
pdf.output("sample_report.pdf")
