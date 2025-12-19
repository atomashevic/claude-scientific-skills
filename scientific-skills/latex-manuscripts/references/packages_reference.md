# LaTeX Packages Reference

Comprehensive reference for LaTeX packages organized by function.

## Encoding and Fonts

### Input Encoding
```latex
\usepackage[utf8]{inputenc}  % UTF-8 input (default in modern LaTeX)
```

### Font Encoding
```latex
\usepackage[T1]{fontenc}     % Better font encoding for accents
\usepackage{lmodern}          % Latin Modern fonts (default)
```

### Font Selection
```latex
\usepackage{times}            % Times Roman
\usepackage{helvet}           % Helvetica
\usepackage{mathptmx}         % Times with math support
```

## Mathematics

### Core Math Packages
```latex
\usepackage{amsmath}          % Enhanced math environments
\usepackage{amssymb}          % Additional math symbols
\usepackage{amsthm}           % Theorem environments
\usepackage{mathtools}        % Extensions to amsmath
```

### Math Environments
```latex
% Single equation
\begin{equation}
  f(x) = x^2
\end{equation}

% Aligned equations
\begin{align}
  x &= a + b \\
  y &= c + d
\end{align}

% Cases
\begin{cases}
  x & \text{if } x > 0 \\
  -x & \text{if } x \leq 0
\end{cases}
```

## Graphics and Figures

### Basic Graphics
```latex
\usepackage{graphicx}         % Include graphics

% Include image
\includegraphics[width=0.8\textwidth]{figure.pdf}
\includegraphics[height=5cm]{image.png}
```

### Subfigures
```latex
\usepackage{subcaption}

\begin{figure}
  \begin{subfigure}[b]{0.48\textwidth}
    \includegraphics[width=\textwidth]{fig1.pdf}
    \caption{First}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.48\textwidth}
    \includegraphics[width=\textwidth]{fig2.pdf}
    \caption{Second}
  \end{subfigure}
  \caption{Overall caption}
\end{figure}
```

## Tables

### Professional Tables
```latex
\usepackage{booktabs}         % Professional table rules

\begin{tabular}{lcc}
  \toprule
  Header 1 & Header 2 & Header 3 \\
  \midrule
  Data 1 & Data 2 & Data 3 \\
  \bottomrule
\end{tabular}
```

### Advanced Tables
```latex
\usepackage{tabularx}         % Full-width tables
\usepackage{longtable}        % Multi-page tables
\usepackage{multirow}         % Multi-row cells
```

## Layout and Formatting

### Page Layout
```latex
\usepackage[margin=1in]{geometry}  % Page margins
```

### Line Spacing
```latex
\usepackage{setspace}
\onehalfspacing   % 1.5 spacing
\doublespacing    % Double spacing
```

## References and Citations

### Hyperlinks
```latex
\usepackage[colorlinks=true]{hyperref}
```

### Smart Cross-References
```latex
\usepackage{cleveref}     % Load AFTER hyperref
\cref{fig:example}        % "Figure 1"
```

### Bibliography
```latex
% BibTeX
\usepackage{natbib}
\bibliographystyle{plainnat}
\bibliography{references}

% BibLaTeX (modern)
\usepackage[backend=biber,style=authoryear]{biblatex}
\addbibresource{references.bib}
```

## Package Loading Order

**Recommended order:**
1. Encoding: `inputenc`, `fontenc`
2. Fonts: `lmodern`, `times`
3. Math: `amsmath`, `amssymb`
4. Graphics: `graphicx`, `xcolor`
5. Layout: `geometry`, `setspace`
6. Tables: `booktabs`, `tabularx`
7. References: `hyperref` (near end)
8. Utilities: `cleveref` (after hyperref), `microtype` (last)
