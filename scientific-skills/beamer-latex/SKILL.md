---
name: beamer-latex
description: "Create professional LaTeX Beamer presentations with themed designs. Full support for Beamer themes (Madrid, Berlin, Copenhagen), color themes, overlays, animations, mathematical content, code listings, and citations. Use when creating academic presentations, conference talks, seminars, or thesis defenses that benefit from consistent theming and LaTeX math. For modern minimalistic black/white style, use beamer-latex-modern instead."
allowed-tools: [Read, Write, Edit, Bash]
---

# LaTeX Beamer Presentations

## Overview

Beamer is LaTeX's powerful document class for creating professional presentations. It excels at mathematical content, consistent formatting, and reproducible slides. This skill provides comprehensive guidance for creating themed Beamer presentations with proper structure, styling, and advanced features.

**Key Strength**: Native LaTeX math, version control friendly, professional themed output.

## When to Use This Skill

Use this skill when:
- Creating academic presentations with mathematical equations
- Building conference talks, seminars, or thesis defenses
- You want themed visual styles (colors, decorations)
- Version control and reproducibility are important
- Collaborating with other LaTeX users
- Presenting code, algorithms, or technical content

**For minimalist black/white presentations**, use `beamer-latex-modern` instead.

## Quick Start

### Minimal Working Example

```latex
\documentclass{beamer}

% Theme
\usetheme{Madrid}
\usecolortheme{beaver}

% Remove navigation symbols (optional)
\setbeamertemplate{navigation symbols}{}

% Title information
\title{Your Presentation Title}
\author{Your Name}
\institute{Your Institution}
\date{\today}

\begin{document}

% Title slide
\begin{frame}
  \titlepage
\end{frame}

% Content slide
\begin{frame}{Slide Title}
  \begin{itemize}
    \item First point
    \item Second point
    \item Third point
  \end{itemize}
\end{frame}

\end{document}
```

### Compilation

```bash
# Basic
pdflatex presentation.tex

# With bibliography
pdflatex presentation.tex
biber presentation      # or: bibtex presentation
pdflatex presentation.tex
pdflatex presentation.tex

# Or use latexmk (recommended)
latexmk -pdf presentation.tex
```

## Themes

### Presentation Themes

Beamer includes many built-in themes controlling overall layout:

**Professional/Academic**:
```latex
\usetheme{Madrid}       % Rounded blocks, navigation dots
\usetheme{Berlin}       % Section navigation in header
\usetheme{Copenhagen}   % Minimal, clean
\usetheme{Boadilla}     % Simple footer
\usetheme{Pittsburgh}   % Very minimal
```

**Modern**:
```latex
\usetheme{CambridgeUS}  % Blue theme with gradients
\usetheme{Singapore}    % Minimalist, Asian style
\usetheme{Rochester}    % Very minimal
\usetheme{Antibes}      % Tree navigation
```

**Feature-Rich**:
```latex
\usetheme{AnnArbor}     % Vertical navigation
\usetheme{Bergen}       % Side navigation
\usetheme{Berkeley}     % Left navigation panel
\usetheme{Goettingen}   % Right sidebar
```

### Color Themes

Apply color schemes to any presentation theme:

**Cool Colors**:
```latex
\usecolortheme{default}     % Blue (Beamer default)
\usecolortheme{dolphin}     % Cyan-blue
\usecolortheme{whale}       % Blue with dark accents
\usecolortheme{seagull}     % Grayscale
```

**Warm Colors**:
```latex
\usecolortheme{beaver}      % Red/brown
\usecolortheme{rose}        % Pink/red
\usecolortheme{crane}       % Orange/yellow
```

**Nature Colors**:
```latex
\usecolortheme{orchid}      % Purple
\usecolortheme{lily}        % Light colors
\usecolortheme{spruce}      % Green tones
```

### Font Themes

```latex
\usefonttheme{default}              % Standard
\usefonttheme{serif}                % Serif fonts
\usefonttheme{structurebold}        % Bold structure elements
\usefonttheme{professionalfonts}    % Don't modify math fonts
```

### Theme Combinations

Popular combinations:

```latex
% Professional Blue
\usetheme{Madrid}
\usecolortheme{default}

% Warm Academic
\usetheme{Madrid}
\usecolortheme{beaver}

% Minimal Gray
\usetheme{Copenhagen}
\usecolortheme{seagull}

% Modern Blue
\usetheme{CambridgeUS}
\usecolortheme{dolphin}

% Clean Professional
\usetheme{Boadilla}
\usecolortheme{orchid}
```

### Custom Colors

Define your own colors:

```latex
% Define colors
\definecolor{myblue}{RGB}{0,90,156}
\definecolor{myred}{RGB}{180,40,40}
\definecolor{mygray}{RGB}{100,100,100}

% Apply to theme elements
\setbeamercolor{structure}{fg=myblue}
\setbeamercolor{title}{fg=myblue}
\setbeamercolor{frametitle}{fg=myblue,bg=white}
\setbeamercolor{block title}{fg=white,bg=myblue}
\setbeamercolor{block body}{fg=black,bg=myblue!10}
```

## Essential Packages

```latex
\documentclass{beamer}

% Encoding
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

% Graphics
\usepackage{graphicx}
\graphicspath{{./figures/}}

% Math
\usepackage{amsmath,amssymb,amsthm}

% Tables
\usepackage{booktabs}
\usepackage{multirow}

% Code listings
\usepackage{listings}

% Algorithms
\usepackage{algorithm}
\usepackage{algorithmic}

% Citations
\usepackage[style=authoryear,backend=biber]{biblatex}
\addbibresource{references.bib}

% TikZ graphics
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning}
```

## Frame Basics

### Standard Frame

```latex
\begin{frame}{Slide Title}
  Content goes here
\end{frame}
```

### Frame with Subtitle

```latex
\begin{frame}{Title}{Subtitle}
  Content
\end{frame}
```

### Frame Options

```latex
% Plain frame (no decorations)
\begin{frame}[plain]
  Full-slide content
\end{frame}

% Fragile frame (for verbatim/code)
\begin{frame}[fragile]{Code Example}
  \begin{verbatim}
  code here
  \end{verbatim}
\end{frame}

% Allow frame breaks (for long content)
\begin{frame}[allowframebreaks]{References}
  \printbibliography
\end{frame}

% Shrink content to fit
\begin{frame}[shrink=10]{Dense Content}
  Lots of content
\end{frame}
```

## Content Elements

### Lists

**Itemize**:
```latex
\begin{itemize}
  \item First point
  \item Second point
    \begin{itemize}
      \item Nested point
    \end{itemize}
  \item Third point
\end{itemize}
```

**Enumerate**:
```latex
\begin{enumerate}
  \item First
  \item Second
  \item Third
\end{enumerate}
```

**Description**:
```latex
\begin{description}
  \item[Term 1] Definition
  \item[Term 2] Definition
\end{description}
```

### Columns

**Two Columns**:
```latex
\begin{columns}
  \begin{column}{0.5\textwidth}
    Left column content
  \end{column}
  \begin{column}{0.5\textwidth}
    Right column content
  \end{column}
\end{columns}
```

**Aligned Columns**:
```latex
\begin{columns}[T]  % Top-aligned
  \begin{column}{0.5\textwidth}
    Content
  \end{column}
  \begin{column}{0.5\textwidth}
    Content
  \end{column}
\end{columns}
```

### Blocks

**Standard Blocks**:
```latex
\begin{block}{Block Title}
  Standard block content
\end{block}

\begin{alertblock}{Warning}
  Alert/warning content (typically red)
\end{alertblock}

\begin{exampleblock}{Example}
  Example content (typically green)
\end{exampleblock}
```

**Theorem Environments**:
```latex
\begin{theorem}
  Statement of theorem
\end{theorem}

\begin{proof}
  Proof content
\end{proof}

\begin{definition}
  Definition text
\end{definition}

\begin{lemma}
  Lemma statement
\end{lemma}
```

### Figures

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.8\textwidth]{figure.pdf}
  \caption{Figure caption}
\end{figure}
```

**Side-by-Side**:
```latex
\begin{columns}
  \begin{column}{0.5\textwidth}
    \includegraphics[width=\textwidth]{fig1.pdf}
  \end{column}
  \begin{column}{0.5\textwidth}
    \includegraphics[width=\textwidth]{fig2.pdf}
  \end{column}
\end{columns}
```

### Tables

```latex
\begin{table}
  \centering
  \begin{tabular}{lcc}
    \toprule
    Method & Accuracy & Time \\
    \midrule
    A & 0.85 & 10s \\
    B & 0.92 & 25s \\
    \bottomrule
  \end{tabular}
  \caption{Results comparison}
\end{table}
```

## Overlays and Animations

### Pause

```latex
\begin{frame}{Sequential Reveal}
  First point
  \pause
  Second point
  \pause
  Third point
\end{frame}
```

### Overlay Specifications

```latex
% Items appear sequentially
\begin{itemize}
  \item<1-> First (appears on slide 1+)
  \item<2-> Second (appears on slide 2+)
  \item<3-> Third (appears on slide 3+)
\end{itemize}

% Automatic sequential
\begin{itemize}[<+->]
  \item First
  \item Second
  \item Third
\end{itemize}
```

### Only and Uncover

```latex
\only<1>{Only visible on slide 1}
\only<2>{Only visible on slide 2}

\uncover<2->{Appears on slide 2 and stays}

\visible<3->{Also appears on slide 3, reserves space}
```

### Alert on Specific Slides

```latex
\begin{itemize}
  \item Normal
  \item<2| alert@2> Highlighted on slide 2
  \item Normal
\end{itemize}
```

### Overlay in Figures

```latex
\includegraphics<1>[width=0.8\textwidth]{before.png}
\includegraphics<2>[width=0.8\textwidth]{after.png}
```

## Mathematical Content

### Inline Math

```latex
The equation $E = mc^2$ is famous.
```

### Display Math

```latex
\begin{equation}
  f(x) = \int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
\end{equation}
```

### Aligned Equations

```latex
\begin{align}
  E &= mc^2 \\
  F &= ma \\
  V &= IR
\end{align}
```

### Matrices

```latex
\begin{equation}
  A = \begin{bmatrix}
    a & b \\
    c & d
  \end{bmatrix}
\end{equation}
```

## Code and Algorithms

### Code Listings

```latex
\begin{frame}[fragile]{Python Code}
\begin{lstlisting}[language=Python]
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
\end{lstlisting}
\end{frame}
```

**Custom Styling**:
```latex
\lstset{
  language=Python,
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{green!60!black},
  stringstyle=\color{orange},
  numbers=left,
  numberstyle=\tiny,
  frame=single,
  breaklines=true
}
```

### Algorithms

```latex
\begin{frame}{Algorithm}
\begin{algorithm}[H]
  \caption{Quicksort}
  \begin{algorithmic}[1]
    \REQUIRE Array $A$, indices $low$, $high$
    \IF{$low < high$}
      \STATE $pivot \gets partition(A, low, high)$
      \STATE $quicksort(A, low, pivot-1)$
      \STATE $quicksort(A, pivot+1, high)$
    \ENDIF
  \end{algorithmic}
\end{algorithm}
\end{frame>
```

## Citations

### Setup

```latex
\usepackage[style=authoryear,maxcitenames=2,backend=biber]{biblatex}
\addbibresource{references.bib}
\renewcommand*{\bibfont}{\scriptsize}
```

### Citing

```latex
According to \textcite{smith2020}, the method...
Previous work \parencite{jones2019,brown2021} showed...
```

### Bibliography Slide

```latex
\begin{frame}[allowframebreaks]{References}
  \printbibliography
\end{frame}
```

## Document Structure

### Sections

```latex
\section{Introduction}
\begin{frame}{Introduction}
  Content
\end{frame}

\section{Methods}
\begin{frame}{Methods}
  Content
\end{frame}
```

### Table of Contents

```latex
\begin{frame}{Outline}
  \tableofcontents
\end{frame}
```

### Section Highlights

```latex
% Show TOC at each section start
\AtBeginSection{
  \begin{frame}{Outline}
    \tableofcontents[currentsection]
  \end{frame}
}
```

### Backup Slides

```latex
% End of main presentation
\begin{frame}{Thank You}
  Questions?
\end{frame}

% Backup slides (not counted)
\appendix

\begin{frame}{Backup: Details}
  Additional content for questions
\end{frame}
```

## TikZ Graphics

### Basic Shapes

```latex
\begin{tikzpicture}
  \draw (0,0) rectangle (2,1);
  \draw (3,0.5) circle (0.5);
  \draw[->, thick] (0,0) -- (3,2);
  \node at (1.5,2) {Label};
\end{tikzpicture}
```

### Flowcharts

```latex
\usetikzlibrary{shapes,arrows,positioning}

\begin{tikzpicture}[node distance=2cm]
  \node[rectangle,draw] (start) {Start};
  \node[rectangle,draw,right=of start] (process) {Process};
  \node[rectangle,draw,right=of process] (end) {End};
  
  \draw[->,thick] (start) -- (process);
  \draw[->,thick] (process) -- (end);
\end{tikzpicture}
```

### Overlay with TikZ

```latex
\begin{tikzpicture}
  \draw (0,0) rectangle (4,3);
  \draw<2-> (1,1) circle (0.5);
  \draw<3->[->, thick] (2,1.5) -- (3,2);
\end{tikzpicture>
```

## Advanced Features

### Hyperlinks

```latex
% Internal links
\begin{frame}{Main Result}
  \label{mainresult}
  Content
\end{frame}

\begin{frame}{Reference}
  See \hyperlink{mainresult}{main result}
\end{frame}

% External links
\url{https://example.com}
\href{https://github.com}{GitHub}
```

### QR Codes

```latex
\usepackage{qrcode}

\begin{frame}{Resources}
  \qrcode[height=3cm]{https://doi.org/10.1234/paper}
  
  Scan for full paper
\end{frame}
```

### Speaker Notes

```latex
\usepackage{pgfpages}
\setbeameroption{show notes on second screen=right}

\begin{frame}{Slide}
  Content
  
  \note{
    Speaker notes here
  }
\end{frame}
```

### Handout Mode

```latex
% In preamble for handouts
\documentclass[handout]{beamer}
```

## Compilation

### Standard

```bash
pdflatex presentation.tex
```

### With Bibliography

```bash
pdflatex presentation.tex
biber presentation
pdflatex presentation.tex
pdflatex presentation.tex
```

### Using latexmk

```bash
# Single compilation
latexmk -pdf presentation.tex

# Watch mode
latexmk -pdf -pvc presentation.tex

# Clean
latexmk -c presentation.tex
```

## Troubleshooting

### Missing Fragile

```
Error: Verbatim environment in frame
Solution: Add [fragile] option
```

### Overlay Issues

```
Problem: Content doesn't appear correctly
Solution: Check <n-> syntax, verify overlay specifications
```

### Image Not Found

```
Error: File not found
Solution: Check \graphicspath, verify file exists
```

### Package Conflicts

```
Error: Option clash
Solution: Load packages only once, check order
```

## Templates

Ready-to-use templates in `assets/`:

- **`beamer_template_basic.tex`**: Minimal starting point
- **`beamer_template_academic.tex`**: Academic conference/seminar template
- **`beamer_template_corporate.tex`**: Corporate/professional style

## Reference Files

Detailed guides in `references/`:

- **`beamer_themes_guide.md`**: Complete theme documentation and gallery
- **`beamer_packages.md`**: Package recommendations and usage
- **`beamer_animations.md`**: Overlay and animation techniques
- **`beamer_troubleshooting.md`**: Common errors and solutions
- **`beamer_compilation.md`**: Compilation workflows and tools

## Best Practices

### Do

✅ Use consistent theme throughout
✅ Keep equations large and readable
✅ Use progressive disclosure (overlays)
✅ Include slide numbers
✅ Use vector graphics (PDF)
✅ Test on actual projector
✅ Prepare backup slides

### Don't

❌ Mix too many fonts or colors
❌ Fill slides with dense text
❌ Use tiny fonts
❌ Forget [fragile] for code
❌ Ignore compilation warnings
❌ Skip practice runs

## Integration with Other Skills

- **latex-manuscripts**: Consistent LaTeX conventions
- **scientific-visualization**: Create figures with matplotlib
- **citation-management**: BibTeX reference management
- **beamer-latex-modern**: Alternative minimalist style
