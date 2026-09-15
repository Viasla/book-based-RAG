import sys

from pypdf import PdfReader, PdfWriter

input_file = sys.argv[1]
output_file = sys.argv[2]

samples = list(map(int, sys.argv[3:]))

input_pdf = PdfReader(input_file)

output_pdf = PdfWriter()

for page in samples:
    output_pdf.add_page(input_pdf.pages[page - 1])

output_pdf.write(output_file)