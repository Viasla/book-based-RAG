import argparse

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption


def convert_default(source, destination):
    converter = DocumentConverter()
    result = converter.convert(source)
    result.document.save_as_markdown(destination)

def convert_options(source, destination):
    pipeline_options = PdfPipelineOptions()

    pipeline_options.do_formula_enrichment = True
    pipeline_options.do_table_structure = True
    pipeline_options.do_ocr = False
    pipeline_options.force_backend_text = True

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options
            )
        }
    )

    result = converter.convert(source)
    result.document.save_as_markdown(destination)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="path to input file")
    parser.add_argument("output", type=str, help="path to output file")
    parser.add_argument("--method", type=str, default="default", help="")

    args = parser.parse_args()

    if args.method == "default":
        convert_default(args.input, args.output)
    elif args.method == "options":
        convert_options(args.input, args.output)
    else:
        print(f"Unknown method: {args.method}")