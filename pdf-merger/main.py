from PyPDF2 import PdfWriter

import os
print("\n***\n")
print(os.path.dirname(__file__))
print(os.listdir())

merger = PdfWriter()
pdfs = []

n = int(input("\nenter no.of pdf to be merged : \n"))

for i in range (0,n):
    name = input(f"enter name of pdf {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)



merger.write("merged-pdf.pdf")
merger.close()