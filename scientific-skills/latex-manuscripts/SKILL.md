---
name: latex-manuscripts
description: "Write scientific manuscripts in LaTeX. Document classes, essential packages, figures/tables, mathematical typesetting, bibliography management (BibTeX/BibLaTeX), cross-references, compilation workflows. For technical LaTeX authoring of research papers, theses, and dissertations. Use with scientific-writing for content and venue-templates for journal-specific formatting."
---

# LaTeX Manuscripts for Scientific Writing

## Overview

LaTeX is the standard typesetting system for scientific manuscripts, offering precise control over document formatting, mathematical notation, figures, tables, and bibliographies. This skill provides comprehensive guidance for writing research papers, theses, and dissertations in LaTeX, covering document structure, essential packages, figures, tables, equations, references, and compilation workflows.

**This skill focuses on the technical LaTeX aspects of manuscript authorship.** For content guidance (IMRAD structure, writing style), use the `scientific-writing` skill. For journal-specific templates, use the `venue-templates` skill.

## When to Use This Skill

This skill should be used when:
- Writing research papers, journal articles, or conference papers in LaTeX
- Creating theses or dissertations
- Typesetting complex mathematical equations
- Managing figures, tables, and cross-references
- Setting up bibliography systems (BibTeX, BibLaTeX)
- Troubleshooting LaTeX compilation errors
- Collaborating on LaTeX documents (Overleaf, Git)
- Converting between document classes or formats
- Optimizing LaTeX documents for submission

## Quick Start

### Minimal Article Template

```latex
\documentclass[12pt,a4paper]{article}

% Essential packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage[colorlinks=true]{hyperref}
\usepackage{natbib}

% Document info
\title{Your Paper Title}
\author{Author Name\\Institution}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
Your abstract goes here.
\end{abstract}

\section{Introduction}
Your introduction text.

\section{Methods}
Your methods.

\section{Results}
Your results.

\section{Discussion}
Your discussion.

\section{Conclusions}
Your conclusions.

\bibliographystyle{plainnat}
\bibliography{references}

\end{document}
```

### Compilation

```bash
# Basic compilation
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex

# Or use latexmk (recommended)
latexmk -pdf manuscript.tex
```

## Core Capabilities

### 1. Document Classes

Choose the appropriate document class for your manuscript type.

**Standard Classes:**

| Class | Use Case | Options |
|-------|----------|---------|
| `article` | Short papers, journal articles | Single-sided, no chapters |
| `report` | Longer reports, theses | Chapters, single-sided |
| `book` | Books, dissertations | Chapters, two-sided |
| `letter` | Correspondence | Letter format |

**Common Class Options:**
```latex
\documentclass[
  12pt,           % Font size (10pt, 11pt, 12pt)
  a4paper,        % Paper size (letterpaper, a4paper)
  twocolumn,      % Two-column layout
  twoside,        % Two-sided printing
  draft,          % Draft mode (faster, shows overfull boxes)
  final           % Final mode (default)
]{article}
```

**Specialized Classes:**
- `revtex4-2` - Physical Review journals
- `elsarticle` - Elsevier journals
- `IEEEtran` - IEEE publications
- `acmart` - ACM publications
- `svjour3` - Springer journals
- `amsart` - AMS mathematical journals
- `memoir` - Flexible book/thesis class

**Example - Two-column IEEE paper:**
```latex
\documentclass[journal,twocolumn]{IEEEtran}
```

### 2. Essential Packages

Load these packages for most scientific manuscripts:

```latex
% Encoding and fonts
\usepackage[utf8]{inputenc}     % UTF-8 input encoding
\usepackage[T1]{fontenc}        % Font encoding for accents
\usepackage{lmodern}            % Modern Latin fonts

% Mathematics
\usepackage{amsmath}            % Enhanced math environments
\usepackage{amssymb}            % Math symbols
\usepackage{amsthm}             % Theorem environments
\usepackage{mathtools}          % Extensions to amsmath

% Graphics and figures
\usepackage{graphicx}           % Include graphics
\usepackage{xcolor}             % Colors
\usepackage{subcaption}         % Subfigures
\usepackage{float}              % Float positioning [H]

% Tables
\usepackage{booktabs}           % Professional tables
\usepackage{tabularx}           % Full-width tables
\usepackage{multirow}           % Multi-row cells
\usepackage{longtable}          % Multi-page tables

% Layout and formatting
\usepackage[margin=1in]{geometry}  % Page margins
\usepackage{setspace}           % Line spacing
\usepackage{microtype}          % Micro-typography
\usepackage{fancyhdr}           % Custom headers/footers

% References and links
\usepackage{hyperref}           % Hyperlinks
\usepackage{cleveref}           % Smart cross-references
\usepackage{natbib}             % Bibliography (author-year)

% Utility
\usepackage{lipsum}             % Dummy text
\usepackage{enumitem}           % List customization
\usepackage{siunitx}            % SI units
```

**Package loading order matters!** Load `hyperref` near the end (but before `cleveref`).

### 3. Figures and Graphics

Include and position figures effectively.

**Basic Figure:**
```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/my_figure.pdf}
  \caption{Figure caption describing what is shown.}
  \label{fig:my_figure}
\end{figure}
```

**Position Specifiers:**
| Specifier | Meaning |
|-----------|---------|
| `h` | Here (approximately) |
| `t` | Top of page |
| `b` | Bottom of page |
| `p` | Separate float page |
| `!` | Override internal parameters |
| `H` | Exactly here (requires `float` package) |

**Recommended:** Use `[htbp]` and let LaTeX decide optimal placement.

**Subfigures:**
```latex
\usepackage{subcaption}

\begin{figure}[htbp]
  \centering
  \begin{subfigure}[b]{0.48\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig_a.pdf}
    \caption{First condition}
    \label{fig:cond_a}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.48\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig_b.pdf}
    \caption{Second condition}
    \label{fig:cond_b}
  \end{subfigure}
  \caption{Overall caption for both figures.}
  \label{fig:both}
\end{figure}
```

**Figure Best Practices:**
- Use vector formats (PDF, EPS) for diagrams and plots
- Use high-resolution (300+ DPI) for photographs
- Keep consistent styling across all figures
- Reference as `Figure~\ref{fig:label}` (non-breaking space)

### 4. Tables

Create professional-looking tables.

**Basic Table with Booktabs:**
```latex
\usepackage{booktabs}

\begin{table}[htbp]
  \centering
  \caption{Comparison of methods.}
  \label{tab:comparison}
  \begin{tabular}{lcc}
    \toprule
    Method & Accuracy (\%) & Time (s) \\
    \midrule
    Baseline & 85.2 & 12.3 \\
    Proposed & \textbf{92.1} & 15.7 \\
    State-of-art & 90.5 & 45.2 \\
    \bottomrule
  \end{tabular}
\end{table}
```

**Column Types:**
| Type | Alignment | Description |
|------|-----------|-------------|
| `l` | Left | Left-aligned |
| `c` | Center | Centered |
| `r` | Right | Right-aligned |
| `p{width}` | Left | Fixed width, top-aligned |
| `m{width}` | Left | Fixed width, vertically centered |
| `X` | Justified | Expanding (tabularx) |

**Multi-row and Multi-column:**
```latex
\usepackage{multirow}

\begin{tabular}{lcc}
  \toprule
  & \multicolumn{2}{c}{Results} \\
  \cmidrule(lr){2-3}
  Method & Metric 1 & Metric 2 \\
  \midrule
  \multirow{2}{*}{Group A} & 85.2 & 90.1 \\
                           & 86.3 & 89.5 \\
  \bottomrule
\end{tabular}
```

**Full-width Table:**
```latex
\usepackage{tabularx}

\begin{table*}[htbp]
  \centering
  \caption{Full-width table spanning both columns.}
  \begin{tabularx}{\textwidth}{lXXX}
    \toprule
    Method & Description & Results & Comments \\
    \midrule
    A & Long description text & Good & Notes here \\
    B & Another description & Better & More notes \\
    \bottomrule
  \end{tabularx}
\end{table*}
```

### 5. Mathematical Typesetting

LaTeX excels at mathematical notation.

**Inline vs Display Math:**
```latex
% Inline math (within paragraph)
The equation $E = mc^2$ is famous.

% Display math (centered, numbered)
\begin{equation}
  E = mc^2
  \label{eq:einstein}
\end{equation}

% Display math (not numbered)
\[
  E = mc^2
\]
```

**Common Math Environments:**
```latex
% Single equation
\begin{equation}
  f(x) = ax^2 + bx + c
  \label{eq:quadratic}
\end{equation}

% Multiple aligned equations
\begin{align}
  f(x) &= x^2 + 2x + 1 \\
       &= (x + 1)^2
  \label{eq:expansion}
\end{align}

% Equation array (no alignment)
\begin{gather}
  x + y = z \\
  a + b = c
\end{gather}

% Cases
\begin{equation}
  f(x) = \begin{cases}
    x^2 & \text{if } x \geq 0 \\
    -x^2 & \text{if } x < 0
  \end{cases}
\end{equation}
```

**Common Math Commands:**
```latex
% Fractions
\frac{a}{b}     % Standard fraction
\tfrac{a}{b}    % Text-style (smaller)
\dfrac{a}{b}    % Display-style (larger)

% Greek letters
\alpha, \beta, \gamma, \delta, \epsilon, \zeta
\Alpha, \Beta, \Gamma, \Delta  % Capital

% Operators
\sum_{i=1}^{n} x_i
\prod_{i=1}^{n} x_i
\int_{0}^{\infty} f(x) \, dx
\lim_{x \to \infty}

% Matrices
\begin{pmatrix}
  a & b \\
  c & d
\end{pmatrix}

% Bold math
\mathbf{x}      % Bold (upright)
\boldsymbol{x}  % Bold (italic)
```

### 6. Bibliography Management

Manage references with BibTeX or BibLaTeX.

**BibTeX (Traditional):**

Create `references.bib`:
```bibtex
@article{smith2023,
  author = {Smith, John and Jones, Mary},
  title = {A Groundbreaking Discovery},
  journal = {Nature},
  year = {2023},
  volume = {600},
  pages = {123--130},
  doi = {10.1038/example}
}

@book{authorbook2020,
  author = {Author, Alice},
  title = {The Complete Guide},
  publisher = {Academic Press},
  year = {2020},
  address = {New York}
}
```

In your document:
```latex
\usepackage{natbib}

% ... document content ...

% Cite references
\citet{smith2023}   % Smith and Jones (2023)
\citep{smith2023}   % (Smith and Jones, 2023)
\cite{smith2023}    % Numbered or author-year depending on style

% Bibliography
\bibliographystyle{plainnat}  % Style: plainnat, abbrvnat, unsrtnat
\bibliography{references}
```

**BibLaTeX (Modern, Recommended):**
```latex
\usepackage[
  backend=biber,
  style=authoryear,
  natbib=true
]{biblatex}
\addbibresource{references.bib}

% ... document content ...

\cite{smith2023}
\parencite{smith2023}  % Parenthetical
\textcite{smith2023}   % Textual

\printbibliography
```

**Compile with BibTeX:**
```bash
pdflatex manuscript
bibtex manuscript
pdflatex manuscript
pdflatex manuscript
```

**Compile with BibLaTeX:**
```bash
pdflatex manuscript
biber manuscript
pdflatex manuscript
pdflatex manuscript
```

### 7. Cross-References

Reference figures, tables, equations, and sections.

**Basic References:**
```latex
\section{Introduction}
\label{sec:intro}

See Section~\ref{sec:intro}.
Equation~\ref{eq:main} shows...
Figure~\ref{fig:result} displays...
Table~\ref{tab:data} presents...
```

**Smart References with cleveref:**
```latex
\usepackage{cleveref}

% Automatic type detection
\cref{fig:result}           % Figure 1
\Cref{fig:result}           % Figure 1 (capitalized)
\cref{eq:main,eq:second}    % Equations 1 and 2
\cref{sec:intro,sec:methods} % Sections 1 and 2
```

**Label Naming Convention:**
- `sec:` - Sections
- `fig:` - Figures
- `tab:` - Tables
- `eq:` - Equations
- `ch:` - Chapters
- `app:` - Appendices

### 8. Document Organization

Structure large documents effectively.

**Single File Structure:**
```latex
\documentclass{article}
% Preamble
\begin{document}

\maketitle
\begin{abstract}...\end{abstract}
\tableofcontents

\section{Introduction}
\section{Methods}
\section{Results}
\section{Discussion}
\section{Conclusions}

\bibliography{references}
\appendix
\section{Supplementary Data}

\end{document}
```

**Multi-File Structure (Recommended for Theses):**

Main file (`thesis.tex`):
```latex
\documentclass{report}
\usepackage{...}

\begin{document}
\include{frontmatter/titlepage}
\include{frontmatter/abstract}
\tableofcontents

\include{chapters/introduction}
\include{chapters/methods}
\include{chapters/results}
\include{chapters/discussion}
\include{chapters/conclusions}

\bibliography{references}
\appendix
\include{appendices/supplementary}
\end{document}
```

Chapter file (`chapters/introduction.tex`):
```latex
\chapter{Introduction}
\label{ch:intro}

Content of introduction...
```

**Input vs Include:**
- `\input{file}` - Insert content (no page break)
- `\include{file}` - Insert content with page breaks, supports `\includeonly`

### 9. Compilation Workflows

Compile LaTeX documents effectively.

**Basic Compilation:**
```bash
pdflatex manuscript.tex
```

**With Bibliography:**
```bash
pdflatex manuscript.tex
bibtex manuscript        # or: biber manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex  # Resolve references
```

**Automated with latexmk (Recommended):**
```bash
# PDF output
latexmk -pdf manuscript.tex

# Continuous compilation (watches for changes)
latexmk -pdf -pvc manuscript.tex

# Clean auxiliary files
latexmk -c manuscript.tex

# Clean all generated files
latexmk -C manuscript.tex
```

**Configure latexmk** (`.latexmkrc`):
```perl
$pdf_mode = 1;
$bibtex_use = 2;
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
```

**Engine Options:**
- `pdflatex` - Standard, fast, good compatibility
- `xelatex` - Unicode, system fonts
- `lualatex` - Unicode, programmable, system fonts

### 10. Common Errors and Solutions

**Undefined Control Sequence:**
```
! Undefined control sequence.
l.42 \includegraphcs
```
*Solution:* Check spelling of command (`\includegraphics`)

**Missing Package:**
```
! LaTeX Error: File `packagename.sty' not found.
```
*Solution:* Install package via TeX Live Manager or MiKTeX

**Overfull/Underfull hbox:**
```
Overfull \hbox (12.3pt too wide) in paragraph at lines 45--50
```
*Solution:* 
- Use `\sloppy` for looser spacing
- Add `\usepackage{microtype}`
- Manually hyphenate: `word\-break`

**Missing $ inserted:**
```
! Missing $ inserted.
```
*Solution:* Use `$...$` around math mode content

**Float Positioning Problems:**
*Solution:*
```latex
% Allow more floats per page
\renewcommand{\topfraction}{0.9}
\renewcommand{\bottomfraction}{0.8}
\renewcommand{\floatpagefraction}{0.7}
\renewcommand{\textfraction}{0.1}
```

**Citation/Reference Warnings:**
```
LaTeX Warning: Citation `smith2023' undefined.
```
*Solution:* Run bibtex/biber and recompile twice

### 11. Collaboration Best Practices

Work effectively with collaborators.

**Overleaf:**
- Real-time collaboration
- Automatic compilation
- Version history
- Comments and track changes

**Git for LaTeX:**
```bash
# .gitignore for LaTeX projects
*.aux
*.bbl
*.blg
*.fdb_latexmk
*.fls
*.log
*.out
*.synctex.gz
*.toc
*.lof
*.lot
```

**One Sentence Per Line:**
```latex
% BAD - hard to diff
This is a long paragraph with multiple sentences that makes it very difficult to see changes in version control because the entire paragraph appears as changed.

% GOOD - easy to diff
This is a long paragraph with multiple sentences.
Each sentence is on its own line.
This makes version control much easier.
Changes are isolated to specific sentences.
```

**Comment Conventions:**
```latex
% TODO: Add results here
% FIXME: Citation needed
% NOTE: Reviewer requested clarification
%% Author1: I suggest rewording this
%% Author2: Agreed, fixed
```

### 12. Thesis/Dissertation Specifics

Additional considerations for longer documents.

**Typical Structure:**
```latex
\documentclass[12pt,oneside]{report}

\begin{document}
% Front matter (roman numerals)
\frontmatter
\include{titlepage}
\include{copyright}
\include{abstract}
\include{dedication}
\include{acknowledgments}
\tableofcontents
\listoffigures
\listoftables

% Main matter (arabic numerals)
\mainmatter
\include{chapter1_intro}
\include{chapter2_background}
\include{chapter3_methods}
\include{chapter4_results}
\include{chapter5_discussion}
\include{chapter6_conclusions}

% Back matter
\backmatter
\bibliography{references}
\appendix
\include{appendix_a}
\include{appendix_b}
\end{document}
```

**Line Spacing:**
```latex
\usepackage{setspace}
\doublespacing  % For draft/review
% or
\onehalfspacing % Common requirement
```

**Page Headers:**
```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{\thepage}
\fancyhead[L]{\leftmark}
```

## Common Workflows

### Workflow 1: Starting a New Paper

1. Choose document class based on target venue
2. Load essential packages (see Section 2)
3. Set up bibliography file (`references.bib`)
4. Create document skeleton with sections
5. Add content iteratively
6. Compile with `latexmk -pdf`

### Workflow 2: Journal Submission

1. Download journal's LaTeX template (or use `venue-templates` skill)
2. Copy template and rename
3. Replace placeholder content
4. Ensure figures are high resolution (300+ DPI)
5. Check page limits and formatting
6. Run final compilation
7. Verify PDF before submission

### Workflow 3: Thesis Writing

1. Create multi-file structure
2. Write chapters individually
3. Use `\includeonly` for faster compilation during writing
4. Add front matter (abstract, acknowledgments, etc.)
5. Generate table of contents, list of figures/tables
6. Final compilation and review

## Integration with Other Skills

This skill works with:

- **scientific-writing**: Content guidance (IMRAD structure, writing style)
- **venue-templates**: Journal-specific templates and requirements
- **latex-posters**: Research poster creation
- **citation-management**: Reference management and BibTeX
- **scientific-visualization**: Creating figures with matplotlib/seaborn

## Reference Files

### references/packages_reference.md
Comprehensive list of LaTeX packages organized by function with usage examples.

### references/math_reference.md
Mathematical typesetting reference including symbols, environments, and common patterns.

### references/troubleshooting.md
Common LaTeX errors and solutions with examples.

### references/thesis_template.tex
Complete thesis template with front matter, chapters, and appendices.

## Scripts

### scripts/check_latex.py
Validate LaTeX document for common issues:
```bash
python scripts/check_latex.py manuscript.tex
```

### scripts/clean_latex.sh
Clean auxiliary files:
```bash
./scripts/clean_latex.sh
```

## Best Practices Summary

1. **Use vector graphics** (PDF, EPS) for figures when possible
2. **Use booktabs** for professional tables
3. **Label consistently** with prefixes (fig:, tab:, eq:, sec:)
4. **One sentence per line** for easier version control
5. **Use latexmk** for automated compilation
6. **Load hyperref last** (before cleveref)
7. **Keep preamble organized** with comments
8. **Use BibLaTeX** for modern bibliography management
9. **Back up regularly** and use version control
10. **Compile frequently** to catch errors early

## Resources

- **CTAN**: https://ctan.org/ - Comprehensive TeX Archive Network
- **Overleaf Documentation**: https://www.overleaf.com/learn
- **LaTeX Wikibook**: https://en.wikibooks.org/wiki/LaTeX
- **TeX StackExchange**: https://tex.stackexchange.com/
- **Detexify**: https://detexify.kirelabs.org/ - Draw symbols to find LaTeX commands
