---
name: beamer-latex-modern
description: "Create clean, minimalistic LaTeX Beamer presentations with black-on-white sans-serif design. Features 16:9 aspect ratio, Helvetica font family, no navigation symbols, subtle frame titles with horizontal rules, custom commands for full-slide images and tight tables. Ideal for modern academic seminars, talks, and conferences where visual clarity and professional minimalism are prioritized. For themed Beamer presentations, use beamer-latex instead."
allowed-tools: [Read, Write, Edit, Bash]
---

# Modern Minimalist Beamer Presentations

## Overview

This skill provides templates and guidance for creating clean, modern LaTeX Beamer presentations with a minimalistic black-on-white design. The style emphasizes content over decoration, using sans-serif typography, generous white space, and subtle visual elements to create professional academic presentations.

**Design Philosophy**: Less is more. Remove all unnecessary elements to let your content shine.

## When to Use This Skill

Use this skill when:
- Creating academic seminars, conference talks, or thesis defenses
- You want a clean, modern, distraction-free presentation style
- Projecting in well-lit rooms where high contrast is essential
- Your content includes text, figures, tables, and occasional equations
- You prefer minimalism over themed/colored presentations
- You want full-slide image support for visual impact

**For themed presentations** with colors and decorations, use the `beamer-latex` skill instead.

## Key Features

### Visual Design
- **16:9 aspect ratio** (widescreen, modern projectors)
- **Black on white** color scheme (maximum contrast)
- **Sans-serif typography** (Helvetica font family)
- **No navigation symbols** (clean, uncluttered)
- **No headline/footline** (full content area)
- **Subtle frame titles** with horizontal rule separator
- **Comfortable margins** (8mm text margins)

### Custom Commands
- `\FullSlideImage{filename}` - Full-page image slides using TikZ overlay
- `\TightTableSetup` - Compact table formatting for wide tables

### Clean Elements
- Simple bullets: `•` for items, `–` for subitems
- Arabic numerals for enumeration
- No colored blocks or backgrounds
- Minimal visual noise

## Quick Start

### 1. Copy the Template

Use the main template from `assets/beamer_modern_template.tex`:

```latex
\documentclass[aspectratio=169,11pt]{beamer}

% --- Minimalistic, sans, black/white beamer style ---
\usetheme{default}
\usecolortheme{default}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}

\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{ragged2e}
\usepackage{hyperref}
\usepackage{tikz}
\usetikzlibrary{calc}

\graphicspath{{figures/}}
\setbeamertemplate{navigation symbols}{}

% Colors: plain black on white
\setbeamercolor{structure}{fg=black}
\setbeamercolor{normal text}{fg=black,bg=white}
\setbeamercolor{frametitle}{fg=black,bg=white}
\setbeamercolor{block title}{fg=black,bg=white}
\setbeamercolor{block body}{fg=black,bg=white}
\setbeamercolor{background canvas}{bg=white}

% Remove headline/footline
\setbeamertemplate{headline}{}
\setbeamertemplate{footline}{}

% Comfortable margins
\setbeamersize{text margin left=8mm,text margin right=8mm}

% Clean frametitle with rule
\setbeamertemplate{frametitle}{%
  \vspace*{0.55em}%
  {\Large\bfseries\insertframetitle\par}%
  \vspace*{0.20em}\hrule\vspace*{0.55em}%
}

% Cleaner bullets
\setbeamertemplate{itemize item}{\textbullet}
\setbeamertemplate{itemize subitem}{\textendash}
\setbeamertemplate{enumerate item}{\arabic{enumi}.}

% Full-slide image helper
\newcommand{\FullSlideImage}[1]{%
  \begin{frame}[plain]
    \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=center] at (current page.center) {%
        \includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{#1}%
      };
    \end{tikzpicture}
  \end{frame}
}

% Tight table defaults
\newcommand{\TightTableSetup}{%
  \setlength{\tabcolsep}{4pt}%
  \renewcommand{\arraystretch}{1.15}%
}

\title[Short Title]{Your Presentation Title}
\subtitle{Subtitle or Context}
\author{Your Name}
\institute{Your Institution}
\date{Event Name\\Date}

\begin{document}

% Title slide
\FullSlideImage{title_slide.png}
% Or use: \begin{frame}[plain]\titlepage\end{frame}

% Content slides
\begin{frame}{Slide Title}
\begin{itemize}
  \item First point
  \item Second point
  \item Third point
\end{itemize}
\end{frame}

\end{document}
```

### 2. Compile

```bash
# Basic compilation
pdflatex presentation.tex

# With bibliography
pdflatex presentation.tex
bibtex presentation
pdflatex presentation.tex
pdflatex presentation.tex

# Or use latexmk (recommended)
latexmk -pdf presentation.tex
```

## Template Variants

### Conference Talk (15-20 minutes)
Use `assets/beamer_modern_conference.tex` for focused, fast-paced talks.

### Academic Seminar (45-60 minutes)
Use `assets/beamer_modern_seminar.tex` for comprehensive coverage.

### Thesis Defense (60+ minutes)
Use `assets/beamer_modern_defense.tex` for formal academic defenses.

## Core Design Elements

### Frame Title Style

The modern template uses a clean frame title with a horizontal rule:

```latex
\setbeamertemplate{frametitle}{%
  \vspace*{0.55em}%
  {\Large\bfseries\insertframetitle\par}%
  \vspace*{0.20em}\hrule\vspace*{0.55em}%
}
```

This creates:
- Bold, large title text
- Subtle horizontal line separator
- Consistent vertical spacing

### Full-Slide Images

Use the `\FullSlideImage` command for impactful visual slides:

```latex
% Single full-slide image
\FullSlideImage{figures/methodology_diagram.png}

% Multiple image slides
\FullSlideImage{figures/result1.png}
\FullSlideImage{figures/result2.png}
```

**How it works**: Uses TikZ overlay to place the image centered on the page, bypassing Beamer's text margins. This prevents cropping or shifting that can occur with standard `\includegraphics`.

**Best practices**:
- Use high-resolution images (1920×1080 or higher for 16:9)
- PNG or PDF format recommended
- Include text/annotations directly in the image for full control
- Great for title slides, methodology diagrams, key results

### Tight Tables

For wide tables that might otherwise overflow:

```latex
\begin{frame}{Results Summary}
\TightTableSetup
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}X ccc@{}}
\toprule
\textbf{Method} & \textbf{Accuracy} & \textbf{F1} & \textbf{Time} \\
\midrule
Baseline & 0.82 & 0.79 & 10s \\
Proposed & \textbf{0.94} & \textbf{0.92} & 15s \\
\bottomrule
\end{tabularx}
\end{frame}
```

The `\TightTableSetup` command:
- Reduces column padding (`\tabcolsep` to 4pt)
- Slightly increases row spacing (`\arraystretch` to 1.15)
- Prevents wide tables from spilling or cropping

## Slide Patterns

### Standard Content Slide

```latex
\begin{frame}{Motivation}
\begin{enumerate}
  \item \textbf{Post-API scarcity}\\
  Major platforms are locking down APIs.
  \item \textbf{Research bottleneck}\\
  These gaps stall research.
  \item \textbf{Synthetic data}\\
  Creating artificial communities via ABMs.
\end{enumerate}
\end{frame}
```

### Two-Column Layout

```latex
\begin{frame}{Comparison}
\begin{columns}[T]
  \begin{column}{0.48\textwidth}
    \textbf{Approach A}
    \begin{itemize}
      \item Feature 1
      \item Feature 2
    \end{itemize}
  \end{column}
  \begin{column}{0.48\textwidth}
    \textbf{Approach B}
    \begin{itemize}
      \item Feature 1
      \item Feature 2
    \end{itemize}
  \end{column}
\end{columns}
\end{frame}
```

### Block with Highlight

```latex
\begin{frame}{Research Question}
\begin{enumerate}
  \item Context point 1
  \item Context point 2
\end{enumerate}

\vspace{0.55em}
\begin{block}{Guiding Question}
Can LLM-agent simulations reproduce known social-media patterns?
\end{block}
\end{frame}
```

### Quote Slide

```latex
\begin{frame}{Example Text}
\small
\justifying
\begin{quote}
It's another example of Microsoft having its head in its clouds, 
thinking it knows what people want before they want it...
\end{quote}

\vspace{0.6em}
\textbf{Similarity:} 0.68
\end{frame}
```

### Results Table

```latex
\begin{frame}{Topics: 78\% Coverage}
\TightTableSetup
\footnotesize
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}X r >{\raggedright\arraybackslash}X r@{}}
\toprule
\textbf{Simulation Topic} & \textbf{\# Docs} & \textbf{Reference Topic} & \textbf{CS} \\
\midrule
AI ethics & 233 & Artificial Intelligence & 0.719 \\
Platform governance & 176 & Social media & 0.708 \\
Data privacy & 75 & Surveillance & 0.722 \\
\bottomrule
\end{tabularx}
\end{frame}
```

## Typography Guidelines

### Font Sizes

| Element | Size | Command |
|---------|------|---------|
| Frame title | Large, bold | Automatic via template |
| Body text | Normal (11pt) | Default |
| Tables | Small/footnotesize | `\small` or `\footnotesize` |
| Captions | Footnotesize | `\footnotesize` |
| References | Tiny/scriptsize | `\tiny` or `\scriptsize` |

### Emphasis

- **Bold** for key terms: `\textbf{important}`
- *Italic* for emphasis: `\emph{emphasis}` or `\textit{text}`
- Avoid underline (poor readability)
- No colored text (maintain black/white aesthetic)

### Text Alignment

```latex
\usepackage{ragged2e}

% Justified text (for quotes, long text)
\justifying
Long paragraph text here...

% Left-aligned (default for lists)
\raggedright
```

## Adding Page Numbers

If you need page numbers (optional), add to the preamble:

```latex
% Simple page numbers in bottom right
\setbeamertemplate{footline}{%
  \hfill\insertframenumber\hspace{2mm}\vspace{2mm}
}

% Or: page X of Y format
\setbeamertemplate{footline}{%
  \hfill\insertframenumber/\inserttotalframenumber\hspace{2mm}\vspace{2mm}
}
```

## Mathematical Content

The template includes standard math support:

```latex
\begin{frame}{Mathematical Model}
The convergence entropy is defined as:
\begin{equation}
  H(x|y) = -\sum_{i} p(x_i|y) \log p(x_i|y)
\end{equation}

where $p(x_i|y)$ is the probability derived from cosine similarity.
\end{frame}
```

For extensive mathematical content, add:

```latex
\usepackage{amsmath,amssymb,amsthm}
```

## Citations and References

### Using BibLaTeX (Recommended)

```latex
% In preamble
\usepackage[style=authoryear,maxcitenames=2,backend=biber]{biblatex}
\addbibresource{references.bib}
\renewcommand*{\bibfont}{\tiny}

% In text
According to \textcite{zhou2025}, the method...
Previous work \parencite{rosen2023} showed...

% References slide
\begin{frame}[allowframebreaks]{References}
  \printbibliography
\end{frame}
```

### Inline References (Simple)

For minimal reference needs, use footnotes:

```latex
\begin{frame}{Limitations}
\begin{enumerate}
  \item Relatively short simulation, single run.
  \item \textbf{No agent memory!}
\end{enumerate}

\vspace{0.8em}
\footnotesize Related: Zhou et al. (2025), \emph{The PIMMUR principles}
\end{frame}
```

## Image Guidelines

### Resolution Requirements

| Use Case | Minimum Resolution | Format |
|----------|-------------------|--------|
| Full-slide images | 1920×1080 (16:9) | PNG, PDF |
| Inline figures | 300 DPI at display size | PDF, PNG |
| Diagrams/schematics | Vector preferred | PDF, SVG |
| Photographs | 300 DPI | PNG, JPG |

### Figure Organization

```latex
\graphicspath{{figures/}}

% Then reference without path:
\FullSlideImage{slide01.png}
\includegraphics[width=0.8\textwidth]{results_chart.pdf}
```

### Creating Full-Slide Images

For best results with `\FullSlideImage`:

1. **Export at 16:9 ratio**: 1920×1080, 2560×1440, or 3840×2160
2. **Include all text in the image**: Titles, labels, annotations
3. **Use consistent styling**: Same fonts, colors across all slides
4. **Consider projection**: High contrast, large text

## Compilation

### Basic Compilation

```bash
pdflatex presentation.tex
```

### With Bibliography

```bash
pdflatex presentation.tex
biber presentation        # or: bibtex presentation
pdflatex presentation.tex
pdflatex presentation.tex
```

### Using latexmk (Recommended)

```bash
# Full compilation with auto-detection
latexmk -pdf presentation.tex

# Continuous mode (watches for changes)
latexmk -pdf -pvc presentation.tex

# Clean auxiliary files
latexmk -c presentation.tex
```

### Engine Options

```bash
# Standard (fastest, good compatibility)
pdflatex presentation.tex

# Better Unicode and font support
lualatex presentation.tex
xelatex presentation.tex
```

## Troubleshooting

### Image Not Filling Slide

**Problem**: `\FullSlideImage` doesn't fill the entire slide.

**Solution**: Ensure image aspect ratio matches 16:9 (1.778:1). The command uses `keepaspectratio` to prevent distortion.

### TikZ Overlay Issues

**Problem**: Full-slide images appear behind other content.

**Solution**: Ensure `\FullSlideImage` creates its own frame with `[plain]` option. Don't mix with other content.

### Font Substitution

**Problem**: Helvetica not available, falls back to different font.

**Solution**: Install `texlive-fonts-recommended` or use alternative:

```latex
% Alternative sans-serif fonts
\usepackage{libertinus}
\usepackage{sourcesanspro}
\usepackage{roboto}
```

### Wide Tables Overflow

**Problem**: Tables extend beyond slide margins.

**Solution**: Use `\TightTableSetup`, `\small` or `\footnotesize`, and `tabularx` with `X` columns:

```latex
\TightTableSetup
\footnotesize
\begin{tabularx}{\textwidth}{@{}lXXX@{}}
...
\end{tabularx}
```

### Horizontal Rule Too Wide/Narrow

**Problem**: Frame title rule doesn't look right.

**Solution**: Adjust in template:

```latex
\setbeamertemplate{frametitle}{%
  \vspace*{0.55em}%
  {\Large\bfseries\insertframetitle\par}%
  \vspace*{0.20em}%
  {\color{black!50}\hrule height 0.5pt}%  % Thinner, grayed rule
  \vspace*{0.55em}%
}
```

## Best Practices

### Content
- **One idea per slide**: Don't overcrowd
- **Minimal text**: Bullets as prompts, you provide explanation
- **Visual balance**: 40-50% figures, 50-60% text
- **Consistent structure**: Same layout patterns throughout

### Design
- **Embrace white space**: Don't fill every corner
- **High contrast**: Black on white works in any lighting
- **Large text**: Readable from back of room
- **Quality images**: High resolution, clean styling

### Workflow
- **Prepare images first**: Create all figures before slides
- **Use full-slide images strategically**: For key diagrams, results
- **Test projection**: Check readability on actual projector
- **Practice timing**: ~1 minute per slide

## Integration with Other Skills

This skill works with:

- **scientific-schematics**: Generate publication-quality diagrams for full-slide images
- **scientific-visualization**: Create matplotlib/seaborn figures
- **latex-manuscripts**: Consistent LaTeX conventions
- **citation-management**: BibTeX reference management

## Reference Files

- `references/modern_design_principles.md`: Design philosophy and rationale
- `references/typography_guide.md`: Font selection and sizing
- `references/full_slide_images.md`: TikZ overlay techniques
- `references/table_formatting.md`: Clean table styling

## Templates

- `assets/beamer_modern_template.tex`: Main template with all features
- `assets/beamer_modern_conference.tex`: 15-20 minute conference talk
- `assets/beamer_modern_seminar.tex`: 45-60 minute academic seminar
- `assets/beamer_modern_defense.tex`: Thesis/dissertation defense

## Example: Complete Presentation Structure

```latex
\documentclass[aspectratio=169,11pt]{beamer}
% ... preamble from template ...

\begin{document}

% Title (as image for visual control)
\FullSlideImage{figures/title_slide.png}

% Motivation
\begin{frame}{Motivation}
\begin{enumerate}
  \item \textbf{Problem context}\\
  Description of the problem.
  \item \textbf{Research gap}\\
  What's missing in current approaches.
  \item \textbf{Our contribution}\\
  What this work provides.
\end{enumerate}
\end{frame}

% Methods (as image for complex diagrams)
\FullSlideImage{figures/methodology.png}

% Results
\begin{frame}{Key Results}
\TightTableSetup
\small
\begin{tabularx}{\textwidth}{@{}lXcc@{}}
\toprule
\textbf{Method} & \textbf{Description} & \textbf{Accuracy} & \textbf{Time} \\
\midrule
Baseline & Standard approach & 0.82 & 10s \\
Ours & Proposed method & \textbf{0.94} & 15s \\
\bottomrule
\end{tabularx}

\vspace{0.8em}
Key finding: Our method achieves 12\% improvement.
\end{frame}

% Result visualization
\FullSlideImage{figures/results_chart.png}

% Conclusions
\begin{frame}{Conclusions}
\begin{enumerate}
  \item Main finding 1
  \item Main finding 2
  \item Future directions
\end{enumerate}

\vspace{0.55em}
\begin{block}{Take-home message}
One sentence summary of the key contribution.
\end{block}
\end{frame}

\end{document}
```
