# Essential Beamer Packages

## Overview

While Beamer includes many features by default, additional packages extend functionality for mathematical content, code listings, citations, graphics, and more. This guide covers essential packages for scientific presentations.

## Core Packages

### Encoding and Fonts

```latex
\usepackage[utf8]{inputenc}    % UTF-8 input encoding
\usepackage[T1]{fontenc}       % Font encoding for accents
```

**Why**: Enables proper handling of accented characters, special symbols, and non-ASCII text.

### Graphics

```latex
\usepackage{graphicx}           % Include graphics
\graphicspath{{./figures/}}     % Set graphics path
```

**Why**: Essential for including figures, images, and diagrams.

**Usage**:
```latex
\includegraphics[width=0.8\textwidth]{figure.pdf}
```

## Mathematical Packages

### Basic Math

```latex
\usepackage{amsmath}            % Enhanced math environments
\usepackage{amssymb}           % Math symbols
\usepackage{amsthm}            % Theorem environments
```

**Why**: Standard packages for mathematical typesetting.

**Features**:
- `align`, `gather`, `multline` environments
- Extended symbol library
- Theorem, proof, definition environments

### Advanced Math

```latex
\usepackage{mathtools}          % Extensions to amsmath
\usepackage{bm}                 % Bold math
```

**Why**: Additional math tools and better bold math support.

## Table Packages

### Professional Tables

```latex
\usepackage{booktabs}          % Professional table rules
\usepackage{multirow}          % Multi-row cells
\usepackage{tabularx}          % Full-width tables
\usepackage{array}             % Enhanced column types
```

**Why**: Create publication-quality tables.

**Usage**:
```latex
\begin{tabular}{lcc}
  \toprule
  Header 1 & Header 2 & Header 3 \\
  \midrule
  Data 1 & Data 2 & Data 3 \\
  \bottomrule
\end{tabular}
```

## Code and Algorithms

### Code Listings

```latex
\usepackage{listings}          % Code listings
\usepackage{xcolor}            % Colors for syntax highlighting
```

**Configuration**:
```latex
\lstset{
  language=Python,
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{green!60!black},
  stringstyle=\color{orange},
  numbers=left,
  frame=single,
  breaklines=true
}
```

**Usage**:
```latex
\begin{frame}[fragile]{Code}
\begin{lstlisting}
def hello():
    print("Hello, World!")
\end{lstlisting}
\end{frame}
```

### Algorithms

```latex
\usepackage{algorithm}         % Algorithm float
\usepackage{algorithmic}       % Algorithmic environment
```

**Usage**:
```latex
\begin{algorithm}[H]
  \caption{Algorithm Name}
  \begin{algorithmic}[1]
    \STATE Step 1
    \STATE Step 2
  \end{algorithmic}
\end{algorithm}
```

## Citation Packages

### BibLaTeX (Recommended)

```latex
\usepackage[style=authoryear,maxcitenames=2,backend=biber]{biblatex}
\addbibresource{references.bib}
\renewcommand*{\bibfont}{\scriptsize}
```

**Why**: Modern, flexible bibliography system.

**Usage**:
```latex
\textcite{smith2020}
\parencite{jones2019}
\printbibliography
```

**Compilation**:
```bash
pdflatex presentation.tex
biber presentation
pdflatex presentation.tex
pdflatex presentation.tex
```

### NatBib (Alternative)

```latex
\usepackage{natbib}
```

**Usage**:
```latex
\citet{smith2020}    % Author (Year)
\citep{smith2020}    % (Author, Year)
\bibliographystyle{plainnat}
\bibliography{references}
```

## Graphics and Drawing

### TikZ

```latex
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,calc}
```

**Why**: Powerful vector graphics for diagrams, flowcharts, plots.

**Usage**:
```latex
\begin{tikzpicture}
  \draw (0,0) rectangle (2,1);
  \node at (1,0.5) {Label};
\end{tikzpicture}
```

### PGFPlots

```latex
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
```

**Why**: Create plots and charts directly in LaTeX.

**Usage**:
```latex
\begin{tikzpicture}
  \begin{axis}[xlabel={$x$}, ylabel={$y$}]
    \addplot coordinates {(0,0) (1,1) (2,4)};
  \end{axis}
\end{tikzpicture}
```

## Hyperlinks

```latex
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  urlcolor=blue,
  citecolor=blue
}
```

**Why**: Clickable links, internal references, PDF bookmarks.

**Usage**:
```latex
\url{https://example.com}
\href{https://github.com}{GitHub}
\hyperlink{label}{text}
```

**Note**: Load `hyperref` near the end of preamble (before `cleveref` if used).

## QR Codes

```latex
\usepackage{qrcode}
```

**Usage**:
```latex
\qrcode[height=3cm]{https://doi.org/10.1234/paper}
```

## Multimedia

```latex
\usepackage{multimedia}
```

**Usage**:
```latex
\movie[width=8cm,height=6cm]{Click to play}{video.mp4}
```

**Note**: Support varies by PDF viewer.

## Text Utilities

### Text Alignment

```latex
\usepackage{ragged2e}          % Better text alignment
```

**Usage**:
```latex
\justifying    % Justified text
\raggedright   % Left-aligned
\raggedleft    % Right-aligned
```

### Text Formatting

```latex
\usepackage{enumitem}          % List customization
```

**Usage**:
```latex
\begin{itemize}[label=\textbullet, leftmargin=*]
  \item Item
\end{itemize}
```

## Specialized Packages

### Units

```latex
\usepackage{siunitx}           % SI units
```

**Usage**:
```latex
\SI{100}{\meter\per\second}
\num{1234.56}
```

### Chemistry

```latex
\usepackage{chemfig}          % Chemical structures
```

### Music

```latex
\usepackage{musixtex}         % Musical notation
```

## Package Loading Order

**Important**: Load packages in this order:

```latex
% 1. Document class
\documentclass{beamer}

% 2. Encoding
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

% 3. Fonts
\usepackage{helvet}  % or other font packages

% 4. Math
\usepackage{amsmath,amssymb,amsthm}

% 5. Graphics
\usepackage{graphicx}
\usepackage{tikz}

% 6. Tables
\usepackage{booktabs}
\usepackage{tabularx}

% 7. Code/Algorithms
\usepackage{listings}
\usepackage{algorithm}

% 8. Citations (near end)
\usepackage[style=authoryear,backend=biber]{biblatex}

% 9. Hyperref (very near end)
\usepackage{hyperref}

% 10. Other utilities
\usepackage{qrcode}
```

## Common Package Conflicts

### hyperref and beamer

**Issue**: Some Beamer features conflict with hyperref
**Solution**: Load hyperref last, use Beamer's built-in hyperlink support when possible

### fontenc and fontspec

**Issue**: Can't use both
**Solution**: Use `fontenc` with pdflatex, `fontspec` with xelatex/lualatex

### babel and biblatex

**Issue**: Language settings may conflict
**Solution**: Load babel before biblatex, configure language options

## Minimal Package Set

For a basic presentation:

```latex
\documentclass{beamer}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{amsmath}
```

## Recommended Package Set

For comprehensive scientific presentations:

```latex
\documentclass{beamer}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{booktabs}
\usepackage{listings}
\usepackage[style=authoryear,backend=biber]{biblatex}
\usepackage{tikz}
\usepackage{hyperref}
```

## Package Installation

### TeX Live

```bash
tlmgr install <package-name>
```

### MiKTeX

Packages typically auto-install on first use, or use Package Manager GUI.

## Summary

**Essential**:
- `graphicx` - Figures
- `amsmath` - Math
- `booktabs` - Tables

**Recommended**:
- `biblatex` - Citations
- `listings` - Code
- `tikz` - Diagrams

**Optional**:
- `qrcode` - QR codes
- `pgfplots` - Plots
- `algorithm` - Algorithms

Choose packages based on your content needs. Don't load unnecessary packages—they slow compilation and can cause conflicts.
