from PyPDF2 import PdfWriter

import glob

files = glob.glob("pdfs/*.pdf")
print(files)

merger = PdfWriter()

for file in files :
    merger.append(file)

merger.write("pdfs/combined_pdf.pdf")
merger.close()