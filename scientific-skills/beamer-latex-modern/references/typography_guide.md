# Typography Guide for Modern Beamer

## Overview

Typography in minimalist presentations is crucial because fonts are the primary visual element. Without colors or decorations, the quality of typography determines the professional appearance of your slides.

## Font Selection

### Primary Font: Helvetica

The modern template uses Helvetica via the `helvet` package:

```latex
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
```

**Why Helvetica?**
- Clean, neutral sans-serif
- Excellent screen readability
- Professional association
- Available in all TeX distributions
- Wide character support

### Alternative Sans-Serif Fonts

If Helvetica is unavailable or you prefer alternatives:

```latex
% Latin Modern Sans (default LaTeX sans)
\usepackage{lmodern}
\renewcommand{\familydefault}{\sfdefault}

% Source Sans Pro (Adobe, modern)
\usepackage{sourcesanspro}

% Roboto (Google, contemporary)
\usepackage{roboto}

% Fira Sans (Mozilla, technical)
\usepackage{FiraSans}

% Libertinus Sans (open source, elegant)
\usepackage{libertinus}
\renewcommand{\familydefault}{\sfdefault}
```

### For Math-Heavy Presentations

Pair sans-serif text with appropriate math fonts:

```latex
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{sfmath}  % Sans-serif math
```

Or use a complete font package:

```latex
\usepackage{newtxsf}  % Times-based sans math
```

## Font Sizes

### Beamer Default Sizes

At 11pt base (our template default):

| Command | Size | Use |
|---------|------|-----|
| `\tiny` | 6pt | Rarely used |
| `\scriptsize` | 8pt | References, fine print |
| `\footnotesize` | 9pt | Captions, table notes |
| `\small` | 10pt | Secondary content, tables |
| `\normalsize` | 11pt | Body text |
| `\large` | 12pt | Emphasis |
| `\Large` | 14pt | Frame titles (template default) |
| `\LARGE` | 17pt | Section headers |
| `\huge` | 20pt | Major emphasis |
| `\Huge` | 25pt | Title slides |

### Recommended Usage

| Element | Size | Notes |
|---------|------|-------|
| Frame title | Large, bold | Set by template |
| Body text | normalsize | Default |
| Bullet points | normalsize | Default |
| Tables | small/footnotesize | Depending on complexity |
| Captions | footnotesize | Clear but subordinate |
| References | scriptsize/tiny | Compact |
| Footnotes | footnotesize | Readable |

### Minimum Readable Sizes

For projection (assume viewing from 10-20 feet):
- **Absolute minimum**: 14pt (footnotesize at 11pt base)
- **Comfortable**: 18pt+ (small at 11pt base)
- **Ideal for key points**: 24pt+ (Large at 11pt base)

## Font Weight

### Bold

Use bold for:
- Frame titles (automatic in template)
- Key terms: `\textbf{important concept}`
- Table headers: `\textbf{Column Name}`
- Emphasis in lists: `\textbf{Point 1}: Description`
- Best results in tables: `\textbf{0.94}`

```latex
\begin{itemize}
  \item \textbf{Finding 1}: Description of first finding
  \item \textbf{Finding 2}: Description of second finding
\end{itemize}
```

### Regular Weight

Use regular weight for:
- Body text
- Descriptions
- Most content

### Avoid

- **Light weights**: Poor visibility on projectors
- **Multiple bold levels**: Creates visual confusion
- **All caps for emphasis**: Use sparingly, if at all

## Emphasis Techniques

### Hierarchy of Emphasis

1. **Size difference**: Most noticeable
2. **Bold weight**: Strong emphasis
3. **Italic**: Subtle emphasis, terms, titles
4. **Spacing**: Isolation draws attention

### Italic

Use italics for:
- Book/paper titles: `\emph{Nature}`
- Technical terms on first use: `\emph{latent variable}`
- Subtle emphasis: `This is \emph{critically} important`
- Mathematical variables in text: variable $x$

```latex
According to \emph{The Design of Everyday Things}, 
visibility is key to usability.
```

### What NOT to Use

- **Underline**: Poor readability, dated appearance
- **Color**: Breaks minimalist aesthetic
- **ALL CAPS**: Shouting, harder to read
- **Multiple fonts**: Creates visual chaos

## Text Alignment

### Left Alignment (Default)

Best for:
- Lists
- Body paragraphs
- Most content

```latex
\begin{itemize}
  \item Point one
  \item Point two
\end{itemize}
```

### Justified Text

Good for:
- Long quotes
- Block text

```latex
\usepackage{ragged2e}
\justifying
Long paragraph text that benefits from justified alignment...
```

### Center Alignment

Use for:
- Titles
- Single lines
- Figures and captions

```latex
\begin{center}
  Centered content
\end{center}
```

### Right Alignment

Rarely used, except for:
- Numbers in tables (use `r` column)
- Date/page numbers

## Line Spacing

### Default Spacing

Beamer's default spacing works well for presentations. Avoid changing unless necessary.

### Adjusting Spacing

For specific needs:

```latex
% Increase spacing in itemize
\setlength{\itemsep}{0.5em}

% Increase spacing in enumerate
\begin{enumerate}
  \setlength{\itemsep}{0.5em}
  \item Item one
  \item Item two
\end{enumerate}
```

### Paragraph Spacing

```latex
% Add space between paragraphs
First paragraph.

\vspace{0.5em}

Second paragraph.
```

## Special Characters

### Dashes

| Character | LaTeX | Use |
|-----------|-------|-----|
| Hyphen | `-` | Compound words: well-known |
| En-dash | `--` | Ranges: 1--10, pages 5--8 |
| Em-dash | `---` | Breaks in thought---like this |

### Quotes

Use proper quotation marks:

```latex
``Quoted text''  % Produces "Quoted text"
`Single quotes'  % Produces 'Single quotes'
```

### Ellipsis

```latex
\ldots  % Produces proper ellipsis: …
```

### Common Symbols

```latex
\%     % Percent sign
\$     % Dollar sign
\&     % Ampersand
\#     % Hash
\_     % Underscore
\textregistered   % ®
\texttrademark    % ™
\textcopyright    % ©
```

## Mathematical Typography

### Inline Math

```latex
The equation $E = mc^2$ shows mass-energy equivalence.
```

### Display Math

```latex
\begin{equation}
  f(x) = \int_{-\infty}^{\infty} e^{-x^2} \, dx
\end{equation}
```

### Math in Sans-Serif Context

For consistency with sans-serif text:

```latex
\usepackage{sfmath}  % Sans-serif math symbols
```

Or selectively:

```latex
\mathsf{text}  % Sans-serif in math mode
```

## Lists Typography

### Bullet Characters

The template uses:
- Level 1: `\textbullet` (•)
- Level 2: `\textendash` (–)

```latex
\setbeamertemplate{itemize item}{\textbullet}
\setbeamertemplate{itemize subitem}{\textendash}
```

### Enumeration

Arabic numerals only:

```latex
\setbeamertemplate{enumerate item}{\arabic{enumi}.}
```

Avoid:
- Roman numerals (i, ii, iii)
- Letters (a, b, c)
- Complex nested numbering

### List Content

- Start items with capital letters
- No periods at end of fragments
- Periods only for complete sentences
- Parallel grammatical structure

```latex
% Good
\begin{itemize}
  \item Collect data from participants
  \item Analyze results using statistical tests
  \item Report findings in standard format
\end{itemize}

% Avoid mixing structures
\begin{itemize}
  \item Data collection
  \item We analyzed the results
  \item Reporting.
\end{itemize}
```

## Encoding and Special Characters

### UTF-8 Support

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
```

This enables:
- Accented characters: é, ñ, ü
- Special symbols: €, £
- Non-English text

### Non-ASCII in Author Names

```latex
\author{José García, François Müller}
```

### Encoding in XeLaTeX/LuaLaTeX

If using XeLaTeX or LuaLaTeX:

```latex
\usepackage{fontspec}
\setmainfont{Helvetica}
\setsansfont{Helvetica}
```

## Troubleshooting

### Font Substitution Warnings

If you see warnings about font substitution:

```
LaTeX Font Warning: Font shape `T1/phv/m/n' undefined
```

Solution: Install the full font package or use an alternative:

```bash
# TeX Live
tlmgr install collection-fontsrecommended

# Or use different font
\usepackage{lmodern}
```

### Math Font Inconsistency

If math looks different from text:

```latex
\usepackage{sfmath}  % Match sans-serif
```

### Character Not Available

If special characters don't render:

```latex
\usepackage[T1]{fontenc}  % Ensure correct encoding
```

## Best Practices Summary

### Do

✅ Use a single font family throughout
✅ Maintain consistent sizes for same-level elements
✅ Use bold for emphasis sparingly
✅ Ensure all text is readable from distance
✅ Use proper typographic characters (–, —, ", ")
✅ Left-align most text content

### Don't

❌ Mix multiple font families
❌ Use fonts smaller than 14pt equivalent
❌ Underline for emphasis
❌ Use all caps extensively
❌ Mix serif and sans-serif randomly
❌ Use decorative or display fonts

## Quick Reference

```latex
% Setup (in preamble)
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}

% Emphasis
\textbf{bold text}
\emph{emphasized text}
{\Large larger text}
{\small smaller text}

% Special characters
``quoted text''
page 1--10
---an aside---
\ldots

% Alignment
\begin{center}...\end{center}
\justifying  % (with ragged2e)
```
