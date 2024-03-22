import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


file_paths = glob.glob('invoices/*.xlsx')

for path in file_paths:
    df = pd.read_excel(path, sheet_name='Sheet 1')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    file_name = Path(path).stem
    invoice_num = file_name.split('-')[0]
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice num.{invoice_num}")
    pdf.output(f"pdfs/{file_name}.pdf")

