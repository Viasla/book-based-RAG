import sys

from docling.document_converter import DocumentConverter


def convert(source, destination):
    converter = DocumentConverter()
    result = converter.convert(source)
    with open(destination, "w", encoding="utf-8") as f:
        f.write(result.document.export_to_markdown())

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert(input_file, output_file)