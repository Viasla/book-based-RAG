import sys

from pypdf import PdfReader, PdfWriter

input_file = sys.argv[1]
output_file = sys.argv[2]

samples = [int(page) - 1 for page in sys.argv[3:]]

input_pdf = PdfReader(input_file)

output_pdf = PdfWriter()

for page in samples:
    output_pdf.add_page(input_pdf.pages[page])

output_pdf.write(output_file)