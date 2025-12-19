# Table Formatting in Modern Beamer

## Overview

Tables in presentations require different treatment than tables in papers. They must be readable from a distance, scannable quickly, and not overwhelming. This guide covers techniques for clean, effective tables in the modern minimalist Beamer style.

## Core Principles

1. **Less is more**: Fewer rows and columns
2. **High contrast**: Clear separation of elements
3. **No clutter**: Minimal lines and decoration
4. **Immediate comprehension**: Key information stands out

## The TightTableSetup Command

### Definition

```latex
\newcommand{\TightTableSetup}{%
  \setlength{\tabcolsep}{4pt}%
  \renewcommand{\arraystretch}{1.15}%
}
```

### Purpose

- **`\tabcolsep`**: Reduces horizontal padding between columns (default 6pt → 4pt)
- **`\arraystretch`**: Slightly increases row height for readability (default 1.0 → 1.15)

### Usage

```latex
\begin{frame}{Results}
\TightTableSetup
\small
\begin{tabular}{lcc}
\toprule
\textbf{Method} & \textbf{Accuracy} & \textbf{Time} \\
\midrule
Baseline & 0.82 & 10s \\
Proposed & \textbf{0.94} & 15s \\
\bottomrule
\end{tabular}
\end{frame}
```

## Essential Packages

```latex
\usepackage{booktabs}    % Professional rules: \toprule, \midrule, \bottomrule
\usepackage{tabularx}    % Full-width tables with X columns
\usepackage{array}       % Enhanced column types
\usepackage{multirow}    % Multi-row cells
```

## Booktabs Rules

**Always use booktabs** for professional appearance:

```latex
\toprule     % Top rule (thicker)
\midrule     % Middle rule (between header and body)
\bottomrule  % Bottom rule (thicker)
\cmidrule    % Partial rules for column groups
```

**Never use**:
- Vertical lines (`|` in column spec)
- `\hline` or `\hline\hline`
- Box-style tables

## Column Alignment

### Basic Types

| Spec | Alignment | Use For |
|------|-----------|---------|
| `l` | Left | Text, labels, descriptions |
| `c` | Center | Categories, status, short items |
| `r` | Right | Numbers (for decimal alignment) |
| `p{width}` | Left, wrapped | Long text |
| `X` | Justified, flex | tabularx: fills remaining space |

### Best Practices

- **Left-align text**: Easier to scan
- **Right-align numbers**: Decimal places line up
- **Center headers**: Works with any content below

### Example

```latex
\begin{tabular}{l r r r}  % Text left, numbers right
\toprule
\textbf{Method} & \textbf{Acc.} & \textbf{F1} & \textbf{Time} \\
\midrule
Baseline A & 0.82 & 0.79 & 10.3s \\
Baseline B & 0.85 & 0.81 & 15.2s \\
Proposed   & 0.94 & 0.92 & 14.7s \\
\bottomrule
\end{tabular}
```

## Font Sizes

For presentations, adjust font size based on table complexity:

| Content | Size | Command |
|---------|------|---------|
| Simple (3-4 rows) | Normal | (default) |
| Medium (5-8 rows) | Small | `\small` |
| Complex (9+ rows) | Footnotesize | `\footnotesize` |

```latex
\TightTableSetup
\footnotesize  % Before the table
\begin{tabular}{...}
```

## Full-Width Tables

Use `tabularx` with `X` columns for tables that should span the text width:

```latex
\begin{tabularx}{\textwidth}{@{}lXcc@{}}
\toprule
\textbf{ID} & \textbf{Description} & \textbf{Value} & \textbf{Status} \\
\midrule
A1 & Long description text that wraps & 42.3 & Yes \\
B2 & Another description here & 18.7 & No \\
\bottomrule
\end{tabularx}
```

**Note**: `@{}` removes outer padding for cleaner alignment with margins.

## Column Spanning

### Multi-Column Headers

```latex
\begin{tabular}{lccc}
\toprule
& \multicolumn{3}{c}{\textbf{Metrics}} \\
\cmidrule(lr){2-4}
\textbf{Method} & \textbf{Acc.} & \textbf{Prec.} & \textbf{Rec.} \\
\midrule
...
\end{tabular}
```

The `\cmidrule(lr){2-4}` creates a partial rule with left and right trimming.

### Multi-Row Cells

```latex
\usepackage{multirow}

\begin{tabular}{llcc}
\toprule
\textbf{Category} & \textbf{Method} & \textbf{Acc.} & \textbf{Time} \\
\midrule
\multirow{2}{*}{Traditional} & Method A & 0.82 & 5s \\
                             & Method B & 0.85 & 8s \\
\midrule
\multirow{2}{*}{Deep Learning} & Method C & 0.91 & 30s \\
                               & Method D & 0.94 & 45s \\
\bottomrule
\end{tabular}
```

## Highlighting

### Bold for Best Results

```latex
Proposed & \textbf{0.94} & \textbf{0.92} & 14.7s \\
```

### Underline for Second Best (Optional)

```latex
Baseline B & \underline{0.85} & \underline{0.81} & 15.2s \\
```

### Color (Use Sparingly in Minimalist Style)

```latex
\usepackage{xcolor}
Proposed & \textcolor{black!60}{0.94} & ...  % Grayed out
```

## Common Table Patterns

### Comparison Table

```latex
\TightTableSetup
\small
\begin{tabular}{l ccc c}
\toprule
\textbf{Method} & \textbf{Acc.} & \textbf{Prec.} & \textbf{Rec.} & \textbf{F1} \\
\midrule
Baseline 1 & 0.82 & 0.80 & 0.78 & 0.79 \\
Baseline 2 & 0.85 & 0.83 & 0.81 & 0.82 \\
Prior SOTA & 0.88 & 0.86 & 0.85 & 0.85 \\
\textbf{Ours} & \textbf{0.94} & \textbf{0.93} & \textbf{0.91} & \textbf{0.92} \\
\bottomrule
\end{tabular}
```

### Hypothesis Results

```latex
\TightTableSetup
\small
\begin{tabular}{l X c c}
\toprule
\textbf{Hyp.} & \textbf{Finding} & \textbf{$p$-value} & \textbf{Supp.} \\
\midrule
H1 & Effect of X on Y & $< 0.001$ & Yes \\
H2 & Moderation by Z & $= 0.023$ & Yes \\
H3 & Interaction effect & $= 0.142$ & No \\
\bottomrule
\end{tabular}
```

### Summary Statistics

```latex
\TightTableSetup
\footnotesize
\begin{tabular}{l cccc}
\toprule
& \textbf{Mean} & \textbf{SD} & \textbf{Min} & \textbf{Max} \\
\midrule
Variable 1 & 45.2 & 12.3 & 18 & 82 \\
Variable 2 & 3.8 & 1.2 & 1 & 7 \\
Variable 3 & 0.67 & 0.21 & 0.12 & 0.98 \\
\bottomrule
\end{tabular}
```

### Topic/Category Coverage

```latex
\TightTableSetup
\footnotesize
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}X r >{\raggedright\arraybackslash}X r@{}}
\toprule
\textbf{Simulation Topic} & \textbf{\#} & \textbf{Reference Topic} & \textbf{Sim.} \\
\midrule
AI ethics & 233 & Artificial Intelligence & 0.72 \\
Platform governance & 176 & Social media & 0.71 \\
Data privacy & 75 & Surveillance & 0.72 \\
\bottomrule
\end{tabularx}
```

## Handling Wide Tables

### Strategy 1: Reduce Column Padding

```latex
\TightTableSetup  % Already reduces tabcolsep
```

### Strategy 2: Smaller Font

```latex
\footnotesize
\begin{tabular}{...}
```

### Strategy 3: Abbreviate Headers

```latex
\textbf{Acc.} instead of \textbf{Accuracy}
\textbf{Prec.} instead of \textbf{Precision}
```

### Strategy 4: Split Into Two Tables

If still too wide, split into two frames with clear titles.

### Strategy 5: Use Full Width

```latex
\begin{tabularx}{\textwidth}{@{}lXXX@{}}
```

## Handling Long Tables

### Multi-Frame Tables

For tables exceeding one slide:

```latex
\begin{frame}{Results (1/2)}
\TightTableSetup
\footnotesize
\begin{tabular}{...}
... first half of rows ...
\end{tabular}
\end{frame}

\begin{frame}{Results (2/2)}
\TightTableSetup
\footnotesize
\begin{tabular}{...}
... second half of rows ...
\end{tabular}
\end{frame}
```

### Recommendation

Avoid multi-frame tables. Instead:
- Show summary/key rows only
- Put full table in backup slides
- Use figures for complex data

## Accessibility

### Readability

- Minimum font size: 14pt equivalent (footnotesize at 11pt base)
- Sufficient row spacing (arraystretch 1.15+)
- Clear contrast (black on white)

### Screen Reader Considerations

For accessible PDFs, ensure:
- Logical reading order
- Clear header row
- Simple structure (avoid complex spanning)

## Complete Example

```latex
\begin{frame}{Performance Comparison}
\TightTableSetup
\small

\begin{center}
\begin{tabular}{l ccc c}
\toprule
& \multicolumn{3}{c}{\textbf{Classification}} & \\
\cmidrule(lr){2-4}
\textbf{Model} & \textbf{Acc.} & \textbf{Prec.} & \textbf{Rec.} & \textbf{Time} \\
\midrule
Random Forest & 0.82 & 0.80 & 0.78 & 2.3s \\
SVM & 0.85 & 0.83 & 0.81 & 5.1s \\
Neural Net & 0.88 & 0.86 & 0.85 & 12.4s \\
\textbf{Proposed} & \textbf{0.94} & \textbf{0.93} & \textbf{0.91} & 8.7s \\
\bottomrule
\end{tabular}
\end{center}

\vspace{0.5em}
\begin{itemize}
  \item Proposed method achieves \textbf{+6\%} accuracy over prior best
  \item Competitive inference time
\end{itemize}
\end{frame}
```

## Summary Checklist

Before finalizing tables:

- [ ] Using booktabs rules (`\toprule`, `\midrule`, `\bottomrule`)
- [ ] No vertical lines
- [ ] Appropriate font size for content amount
- [ ] Key results highlighted (bold)
- [ ] Headers clearly distinguished
- [ ] Aligned appropriately (text left, numbers right)
- [ ] Not too many columns (≤6 recommended)
- [ ] Not too many rows (≤8-10 visible at once)
- [ ] `\TightTableSetup` applied if needed
- [ ] Readable from back of room
