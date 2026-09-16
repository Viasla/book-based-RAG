# Tool Comparison

In this report I gonna compare tools for data extraction from pdf textbooks.

## Tools

- Docling
- Marker
- PyMuPDF

### Scripts

#### Page Selector

In order to select sample pages I wrote script which does just selects pages without changing structure of page.

##### Usage

To select pages run following command from top-level directory of project:
```bash
python scr\pageselector.py <input_pdf> <output_pdf> <pages>  
```

For example:

```bash
python scr\pageselector.py resources\test\rudin.pdf "resources\reports\Tool Comparison\samples\rudin-samples.pdf" 8 9 14 15 16 19 20 23 36 46 51 78
```

#### Docling

#### Marker

#### PyMuPDF

## Books

In order to check tools performance, I chose sample pages (pdf file with selected pages) which represent each problem with each textbook. Table contains page numbers I chose and what will I look for.

### Real and Complex Analysis

[Textbook](../../test/rudin.pdf).

[Sample pages](./samples/rudin-samples.pdf).

|Page|Reason|
|:---|:-----|
|8   |"CONTENTS", contents, "vii" (page counter)|
|9   |"viii CONTENTS" (page counter), contents|
|14  |"PREFACE", regular text (with inline LaTeX), "xiii" (page counter)|
|15  |"xiv PREFACE" (page counter), regular text (with inline LaTeX)|
|16  |"PROLOGUE", "THE EXPONENTIAL FUNCTION", formulas, Theorem (bold and italic text), "1" (page counter)|
|19  |Problematic page, "4 REAL AND COMPLEX ANALYSIS" (page counter), formulas|
|20  |"CHAPTER", "ONE", "ABSTRACT INTEGRATION", "5" (page counter)|
|23  |"8 REAL AND COMPLEX ANALYSIS" (page counter), "The Concept of Measurability" (header), Definitions|
|36  |"ABSTRACT INTEGRATION 21" (page counter), "1.26 Lebesgue's Monotone Convergence Theorem"|
|46  |"ABSTRACT INTEGRATION 31" (page counter), Theorem, Exercises, smaller text|
|51  |"36 REAL AND COMPLEX ANALYSIS", theorems and proofs, footnote|
|78  |"$L^{p}$-SPACES 63", formulas|

#### Docling

[Parsing result]().

#### Marker

[Parsing result]().

#### PyMuPDF

[Parsing result]().