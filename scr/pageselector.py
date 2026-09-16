import sys

from pypdf import PdfReader, PdfWriter


def select_pages(input_file, output_file, samples):
    input_pdf = PdfReader(input_file)
    output_pdf = PdfWriter()
    
    output_pdf.append(input_pdf, samples)

    output_pdf.write(output_file)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    samples = [int(page) - 1 for page in sys.argv[3:]]

    select_pages(input_file, output_file, samples)