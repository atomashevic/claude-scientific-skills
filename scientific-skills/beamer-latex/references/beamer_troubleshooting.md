# Beamer Troubleshooting Guide

## Common Compilation Errors

### Missing Fragile Option

**Error**:
```
! LaTeX Error: Something's wrong--perhaps a missing \item.
```

**Cause**: Using verbatim environments (`verbatim`, `lstlisting`) without `[fragile]` option.

**Solution**:
```latex
\begin{frame}[fragile]{Code Example}
  \begin{verbatim}
  code here
  \end{verbatim}
\end{frame}
```

### Package Option Clash

**Error**:
```
! LaTeX Error: Option clash for package X.
```

**Cause**: Loading the same package multiple times with different options.

**Solution**: Load package only once, combine options:
```latex
% Wrong
\usepackage[option1]{package}
\usepackage[option2]{package}

% Correct
\usepackage[option1,option2]{package}
```

### File Not Found

**Error**:
```
! LaTeX Error: File `figure.pdf' not found.
```

**Cause**: Image file missing or wrong path.

**Solution**:
```latex
% Set graphics path
\graphicspath{{./figures/}{./images/}}

% Or use full path
\includegraphics{./figures/figure.pdf}
```

### Missing Bibliography

**Error**:
```
LaTeX Warning: Citation `smith2020' undefined.
```

**Cause**: Bibliography not processed or file not found.

**Solution**:
```bash
# For BibLaTeX
pdflatex presentation.tex
biber presentation
pdflatex presentation.tex
pdflatex presentation.tex

# For BibTeX
pdflatex presentation.tex
bibtex presentation
pdflatex presentation.tex
pdflatex presentation.tex
```

## Common Warnings

### Overfull/Underfull Boxes

**Warning**:
```
Overfull \hbox (12.3pt too wide) in paragraph at lines 45--50
```

**Cause**: Content too wide for column/slide.

**Solutions**:
```latex
% Allow looser spacing
\sloppy

% Use smaller font
\small
\begin{itemize}
  ...
\end{itemize}

% Break long words
word\-break

% Use microtype
\usepackage{microtype}
```

### Float Placement

**Warning**:
```
LaTeX Warning: Float too large for page
```

**Cause**: Figure/table too large.

**Solution**:
```latex
% Scale down
\includegraphics[width=0.7\textwidth]{figure.pdf}

% Use [H] for exact placement
\usepackage{float}
\begin{figure}[H]
  ...
\end{figure}
```

### Font Substitution

**Warning**:
```
LaTeX Font Warning: Font shape `T1/phv/m/n' undefined
```

**Cause**: Font not installed.

**Solution**:
```bash
# Install fonts
tlmgr install collection-fontsrecommended

# Or use alternative
\usepackage{lmodern}
```

## Overlay Issues

### Overlays Not Working

**Problem**: Content doesn't appear/disappear correctly.

**Solutions**:
- Check syntax: `<1->` vs `<1-2>`
- Ensure proper spacing
- Test with simple example first
- Verify PDF viewer supports overlays

### Too Many Slides

**Problem**: Frame creates unexpected number of overlays.

**Solution**: Review all overlay specifications in frame, simplify logic.

### Navigation Problems

**Problem**: Can't navigate between overlays.

**Solution**: Use arrow keys or mouse clicks. Some PDF viewers don't support overlays—test with Adobe Reader or Okular.

## Theme Issues

### Theme Not Found

**Error**:
```
! LaTeX Error: File `beamerthemeX.sty' not found.
```

**Solution**:
```bash
tlmgr install beamer
```

### Colors Not Applying

**Problem**: Custom colors don't appear.

**Solution**: Load `xcolor`:
```latex
\usepackage{xcolor}
\definecolor{myblue}{RGB}{0,90,156}
```

### Navigation Symbols Appear

**Problem**: Navigation symbols visible when unwanted.

**Solution**:
```latex
\setbeamertemplate{navigation symbols}{}
```

## Math Issues

### Math Not Rendering

**Error**:
```
! Missing $ inserted.
```

**Cause**: Math mode not properly delimited.

**Solution**:
```latex
% Inline math
$E = mc^2$

% Display math
\[
  E = mc^2
\]

% Or
\begin{equation}
  E = mc^2
\end{equation}
```

### Math Font Issues

**Problem**: Math looks different from text.

**Solution**:
```latex
% Match math to text
\usepackage{sfmath}  % Sans-serif math
```

## Table Issues

### Table Too Wide

**Problem**: Table extends beyond slide margins.

**Solutions**:
```latex
% Use smaller font
\small
\begin{tabular}{...}

% Use tabularx for full width
\usepackage{tabularx}
\begin{tabularx}{\textwidth}{...}

% Scale down
\resizebox{\textwidth}{!}{\begin{tabular}{...}}
```

### Table Alignment

**Problem**: Columns not aligned correctly.

**Solution**: Check column specifications:
```latex
% l = left, c = center, r = right
\begin{tabular}{lcc}
  Left & Center & Right \\
\end{tabular}
```

## Figure Issues

### Figure Not Found

**Error**: File not found.

**Solutions**:
- Check file exists
- Verify path is correct
- Use `\graphicspath`
- Check file extension matches

### Figure Too Large/Small

**Problem**: Figure size incorrect.

**Solution**:
```latex
% Scale to width
\includegraphics[width=0.8\textwidth]{figure.pdf}

% Scale to height
\includegraphics[height=0.6\textheight]{figure.pdf}

% Scale both
\includegraphics[width=0.8\textwidth,height=0.6\textheight,keepaspectratio]{figure.pdf}
```

### Low Resolution

**Problem**: Figure appears pixelated.

**Solution**: Use vector formats (PDF, EPS) or high-resolution raster (300+ DPI).

## Bibliography Issues

### Citations Not Resolved

**Problem**: Citations show as [?].

**Solution**: Run bibliography processor:
```bash
pdflatex presentation.tex
biber presentation  # or bibtex
pdflatex presentation.tex
pdflatex presentation.tex
```

### Bibliography Style

**Problem**: Bibliography format not as desired.

**Solution**: Change style:
```latex
% BibLaTeX
\usepackage[style=authoryear]{biblatex}

% BibTeX
\bibliographystyle{plainnat}
```

## Compilation Issues

### Slow Compilation

**Problem**: Compilation takes too long.

**Solutions**:
- Use `draft` mode during development
- Reduce image resolution temporarily
- Use `\includeonly` for large documents
- Compile only changed sections

### Out of Memory

**Error**: TeX capacity exceeded.

**Solutions**:
- Reduce image sizes
- Split into multiple files
- Use `draft` mode
- Increase TeX memory limits

### SyncTeX Issues

**Problem**: PDF sync not working.

**Solution**: Compile with SyncTeX:
```bash
pdflatex -synctex=1 presentation.tex
```

## PDF Viewer Issues

### Overlays Not Working

**Problem**: Can't navigate overlays in PDF.

**Solution**: Use PDF viewer that supports overlays:
- Adobe Reader
- Okular
- Evince (Linux)
- Some browsers don't support overlays

### Links Not Working

**Problem**: Hyperlinks don't work.

**Solution**: Ensure `hyperref` loaded correctly, recompile.

### Fonts Not Embedded

**Problem**: Fonts look wrong in PDF.

**Solution**: Embed fonts:
```bash
pdflatex -dEmbedAllFonts=true presentation.tex
```

## Debugging Tips

### Verbose Output

```latex
\errorcontextlines=999
```

### Draft Mode

```latex
\documentclass[draft]{beamer}
```

Shows overfull boxes, skips images, faster compilation.

### Show Labels

```latex
\usepackage[notref,notcite]{showkeys}
```

Shows all `\label` commands for debugging.

### Check Log File

Review `.log` file for warnings and errors:
```bash
grep -i "warning\|error" presentation.log
```

## Getting Help

### Check Documentation

```bash
texdoc beamer
```

### Online Resources

- TeX StackExchange: https://tex.stackexchange.com/
- Beamer User Guide: `texdoc beamer`
- CTAN: https://ctan.org/pkg/beamer

### Minimal Example

Create minimal example to isolate problem:
```latex
\documentclass{beamer}
\begin{document}
\begin{frame}{Test}
  Test content
\end{frame}
\end{document}
```

## Prevention

### Best Practices

- Compile frequently
- Test on actual presentation computer
- Use version control
- Keep backup copies
- Test bibliography early
- Check all figures exist
- Verify fonts installed

### Template Approach

Start with working template, modify incrementally.

### Incremental Development

Add features one at a time, test after each addition.

## Summary

Most Beamer issues stem from:
1. Missing packages
2. Incorrect syntax
3. File path problems
4. Compilation order (bibliography)
5. PDF viewer limitations

When in doubt: simplify, test, then add complexity.
