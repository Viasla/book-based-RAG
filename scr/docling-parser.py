import argparse

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    EasyOcrOptions,
    OcrMode,
    PdfPipelineOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption


def convert_default(source, destination):
    converter = DocumentConverter()
    result = converter.convert(source)
    result.document.save_as_markdown(destination)

def convert_no_ocr(source, destination):
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

def convert_default_ocr(source, destination):
    pipeline_options = PdfPipelineOptions()

    pipeline_options.do_formula_enrichment = True
    pipeline_options.do_table_structure = True
    pipeline_options.do_ocr = True
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

def convert_easy_ocr(source, destination):
    pipeline_options = PdfPipelineOptions()

    pipeline_options.do_formula_enrichment = True
    pipeline_options.do_table_structure = True
    pipeline_options.do_ocr = True
    pipeline_options.ocr_options = EasyOcrOptions(
        lang=["iso:en"],
        mode=OcrMode.FULL_PAGE,
    )
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
    elif args.method == "no_ocr":
        convert_no_ocr(args.input, args.output)
    elif args.method == "default_ocr":
        convert_default_ocr(args.input, args.output)
    elif args.method == "easy_ocr":
        convert_easy_ocr(args.input, args.output)
    else:
        print(f"Unknown method: {args.method}")