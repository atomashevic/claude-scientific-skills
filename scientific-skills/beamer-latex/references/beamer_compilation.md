# Beamer Compilation Guide

## Overview

Compiling Beamer presentations requires understanding the compilation process, especially when using citations, cross-references, and complex content. This guide covers all compilation methods and workflows.

## Basic Compilation

### Single Pass

```bash
pdflatex presentation.tex
```

**When**: Simple presentations without citations or cross-references.

**Output**: `presentation.pdf`

### Multiple Passes

For citations and cross-references:

```bash
pdflatex presentation.tex
pdflatex presentation.tex
```

**Why**: First pass collects references, second resolves them.

## Compilation with Bibliography

### BibLaTeX Workflow

```bash
pdflatex presentation.tex
biber presentation
pdflatex presentation.tex
pdflatex presentation.tex
```

**Steps**:
1. First `pdflatex`: Collects citations, writes `.aux` file
2. `biber`: Processes bibliography, creates `.bbl` file
3. Second `pdflatex`: Inserts citations
4. Third `pdflatex`: Resolves all cross-references

### BibTeX Workflow

```bash
pdflatex presentation.tex
bibtex presentation
pdflatex presentation.tex
pdflatex presentation.tex
```

**Steps**: Same as BibLaTeX, but use `bibtex` instead of `biber`.

## Using latexmk (Recommended)

### Basic Usage

```bash
latexmk -pdf presentation.tex
```

**Advantages**:
- Automatically detects bibliography needs
- Runs correct number of passes
- Handles dependencies

### Continuous Mode

```bash
latexmk -pdf -pvc presentation.tex
```

**Behavior**: Watches for file changes, recompiles automatically.

**Stop**: Press `Ctrl+C`

### Clean Auxiliary Files

```bash
latexmk -c presentation.tex
```

Removes: `.aux`, `.log`, `.nav`, `.out`, `.snm`, `.toc`, `.bbl`, `.blg`, etc.

### Clean All Generated Files

```bash
latexmk -C presentation.tex
```

Removes all generated files including PDF.

## Compilation Engines

### PDFLaTeX (Default)

```bash
pdflatex presentation.tex
```

**Best for**: Standard LaTeX, fastest compilation.

**Limitations**: Limited Unicode support, system fonts.

### XeLaTeX

```bash
xelatex presentation.tex
```

**Best for**: System fonts, Unicode, complex typography.

**Usage**: Change document class:
```latex
% Not needed, but can specify
\documentclass[xelatex]{beamer}
```

### LuaLaTeX

```bash
lualatex presentation.tex
```

**Best for**: Advanced Lua scripting, Unicode, system fonts.

**Advantages**: Most flexible, programmable.

## Compilation Options

### Draft Mode

```bash
pdflatex -draftmode presentation.tex
```

**Or in document**:
```latex
\documentclass[draft]{beamer}
```

**Effects**:
- Faster compilation
- Skips images
- Shows overfull boxes
- No hyperlinks

### Non-Stop Mode

```bash
pdflatex -interaction=nonstopmode presentation.tex
```

**Behavior**: Doesn't stop for errors, continues compilation.

**Use**: Automated builds, when you want to see all errors.

### Output Directory

```bash
pdflatex -output-directory=build presentation.tex
```

**Effect**: All output files go to `build/` directory.

**Use**: Keep source directory clean.

### SyncTeX

```bash
pdflatex -synctex=1 presentation.tex
```

**Effect**: Creates `.synctex.gz` for PDF-source synchronization.

**Use**: Forward/inverse search in editors.

## Compilation Scripts

### Simple Shell Script

```bash
#!/bin/bash
# compile.sh

FILE="$1"
BASENAME="${FILE%.tex}"

pdflatex "$FILE"
if grep -q "\\bibliography\|\\addbibresource" "$FILE"; then
    biber "$BASENAME"  # or: bibtex "$BASENAME"
    pdflatex "$FILE"
fi
pdflatex "$FILE"
```

**Usage**: `./compile.sh presentation.tex`

### Advanced Script

See `scripts/compile_beamer.sh` for full-featured compilation script with options.

## Troubleshooting Compilation

### Missing Files

**Problem**: Can't find `.sty` files.

**Solution**:
```bash
# Check if package installed
kpsewhich beamerthemeMadrid.sty

# Install if missing
tlmgr install beamer
```

### Compilation Hangs

**Problem**: Compilation never finishes.

**Solutions**:
- Check for infinite loops in TikZ
- Reduce image sizes
- Use `draft` mode
- Check for circular references

### Out of Memory

**Error**: TeX capacity exceeded.

**Solutions**:
- Increase memory limits
- Reduce image sizes
- Split into multiple files
- Use `draft` mode

### Bibliography Not Found

**Problem**: Bibliography processor can't find `.bib` file.

**Solution**: Ensure `.bib` file in same directory or specify path:
```latex
\addbibresource{path/to/references.bib}
```

## Compilation Workflows

### Development Workflow

```bash
# Fast iteration
pdflatex -draftmode presentation.tex

# When ready for final
latexmk -pdf presentation.tex
```

### Collaboration Workflow

```bash
# Clean before sharing
latexmk -c presentation.tex

# Recipient compiles
latexmk -pdf presentation.tex
```

### CI/CD Workflow

```bash
# Non-interactive, all errors shown
pdflatex -interaction=nonstopmode presentation.tex
biber presentation
pdflatex -interaction=nonstopmode presentation.tex
pdflatex -interaction=nonstopmode presentation.tex
```

## latexmk Configuration

### .latexmkrc File

Create `.latexmkrc` in project directory:

```perl
$pdf_mode = 1;
$bibtex_use = 2;  # Use biber
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
```

**Options**:
- `$pdf_mode = 1`: PDF output
- `$bibtex_use = 2`: Use biber
- `$bibtex_use = 1`: Use bibtex
- `$pdflatex`: Custom pdflatex command

## Multi-File Documents

### Using \input

```latex
% main.tex
\input{intro.tex}
\input{methods.tex}
\input{results.tex}
```

**Compilation**: Same as single file.

### Using \include

```latex
% main.tex
\include{intro}
\include{methods}
\include{results}
```

**Compilation**: Same, but can use `\includeonly`:
```latex
\includeonly{intro,results}  % Only compile these
```

## Best Practices

### Compile Frequently

- Catch errors early
- Verify layout
- Test overlays

### Use latexmk

- Automatic dependency handling
- Correct number of passes
- Clean commands

### Version Control

**Include**:
- `.tex` files
- `.bib` files
- `.sty` files (if custom)

**Exclude** (`.gitignore`):
```
*.aux
*.log
*.nav
*.out
*.snm
*.toc
*.bbl
*.blg
*.fdb_latexmk
*.fls
*.synctex.gz
*.pdf  # Optional: if large
```

### Backup Before Major Changes

- Keep working version
- Test compilation after changes
- Use version control

## Summary

**For simple presentations**:
```bash
pdflatex presentation.tex
```

**For presentations with citations**:
```bash
latexmk -pdf presentation.tex
```

**For development**:
```bash
latexmk -pdf -pvc presentation.tex
```

**For production**:
```bash
latexmk -pdf presentation.tex
latexmk -c presentation.tex  # Clean if desired
```

Choose the method that fits your workflow. `latexmk` is recommended for most cases.
