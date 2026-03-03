from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 10)
pdf.cell(95, 6, txt="Time: 3 Hours", ln=0)
pdf.cell(95, 6, txt="Max Marks: 100", ln=1, align="R")
pdf.line(10, pdf.get_y()+2, 200, pdf.get_y()+2)
pdf.ln(8)
pdf.set_font("Arial", size=11)
safe_line = "Time: 3 Hours  Maximum Marks: 60"
pdf.multi_cell(0, 6, txt=safe_line)
print("Success")
