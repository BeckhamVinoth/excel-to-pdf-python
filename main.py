import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


file_paths = glob.glob('invoices/*.xlsx')

for path in file_paths:
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    file_name = Path(path).stem
    invoice_num = file_name.split('-')[0]
    invoice_date = file_name.split('-')[1]
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice num.{invoice_num}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date : {invoice_date}", ln=1)

    df = pd.read_excel(path, sheet_name='Sheet 1')

    # Add a header
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)



    pdf.output(f"pdfs/{file_name}.pdf")

