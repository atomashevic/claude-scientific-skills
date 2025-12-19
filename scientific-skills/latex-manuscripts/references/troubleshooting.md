# LaTeX Troubleshooting Guide

Common errors and their solutions.

## Compilation Errors

### Undefined Control Sequence
**Error:** `! Undefined control sequence.`
**Solution:** Check spelling of commands, ensure packages are loaded

### Missing Package
**Error:** `! LaTeX Error: File 'packagename.sty' not found.`
**Solution:** Install package via `tlmgr install packagename`

### Overfull/Underfull hbox
**Warning:** `Overfull \hbox (12.3pt too wide)`
**Solution:** 
- Use `\sloppy` for looser spacing
- Add `\usepackage{microtype}`
- Manual hyphenation: `word\-break`

### Missing $ Inserted
**Error:** `! Missing $ inserted.`
**Solution:** Use `$...$` around math mode content

## Reference Errors

### Undefined Reference
**Warning:** `Reference 'fig:example' undefined`
**Solution:** Run LaTeX twice, check label spelling

### Citation Undefined
**Warning:** `Citation 'smith2023' undefined`
**Solution:** Run BibTeX/Biber and recompile twice

## Figure/Table Issues

### Figure Not Found
**Error:** `File 'figure.pdf' not found`
**Solution:** Check file path, use `\graphicspath{{./figures/}}`

### Table Too Wide
**Solution:** Use `tabularx` or `\resizebox`

## Quick Fixes Checklist

1. Check spelling of commands
2. Ensure packages are loaded
3. Run LaTeX twice for references
4. Run BibTeX/Biber for citations
5. Check file paths are correct
