import sys

from docling.document_converter import DocumentConverter


def convert(source, destination):
    converter = DocumentConverter()
    result = converter.convert(source)
    result.document.save_as_markdown(destination)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert(input_file, output_file)