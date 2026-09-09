# PDF Analysis

This is report containing pdf analysis of certain textbooks present on the Internet.

Note: I tried to identify possible problems with each textbook, and report only one instance of that type of issue. Throughout textbooks each problem could appear more frequently than once.

## Grinstead and Snell’s Introduction to Probability

[Textbook](../../test/prob.pdf).

### General Analysis

Pages: 518

Digital PDF: Yes

Contains:
- formulas
- diagrams
- images
- tables

Expected difficulty: Medium

### Problematic pages

![Page 11](./prob-problem-1.png)

Reason: ambiguous table, may be mistaken by regular LaTeX formula.

![Page 33](./prob-problem-2.png)

Reason: this diagram could be interpreted as LaTeX formula instead of a regular image.

![Page 59](./prob-problem-3.png)

Reason: ambiguous table, there is no clear separation of columns and rows.


## Read and Complex Analysis

[Textbook](../../test/rudin.pdf).

This book contains many dense LaTeX formulas, which could be extracted incorrectly.

### General Analysis

Pages: 433

Digital PDF: Yes

Contains:
- formulas

Expected difficulty: Easy

### Problematic pages

![Page 4](./rudin-problem-1.png)

Reason: there is a posibility for illformed LaTeX formula.

![Page 5](./rudin-problem-2.png)

Reason: Chapter indication could be interpreted not as intended.

## Set theory and the continuum hypothesis

[Textbook](../../test/conti.pdf).

### General Analysis

Pages: 160

Digital PDF: No

Contains:
- formulas
- tables

Expected difficulty: Hard

### Problematic pages

![Page 10](./conti-problem-1.png)

Reason: page contains irregular LaTeX formula.

![Page 15](./conti-problem-2.png)

Reason: table could be extracted incorrectly

![Page 100](./conti-problem-3.png)

## A First Course in Probability

[Textbook](../../test/a_first_course_in_probability.pdf)

### General Analysis

Pages: 848

Digital PDF: Yes

Contains:
- formulas
- diagrams
- images
- tables

Expected difficulty: Hard

### Problematic pages

![Page 52](./first-problem-1.png)

Reason: "i = 1" is bigger than usually, in that book.

![Page 79](./first-problem-2.png)

Reason: symbols are misaligned, this could pose a threat to correct formula extraction.

![Page 167](./first-problem-3-1.png)
![Page 168](./first-problem-3-2.png)

Reason: can be extracted as two distinct tables.

![Page 556](./first-problem-4.png)

Reason: "i -> - infty" could be interpreted incorrectly.

# Conclusion