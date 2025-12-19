# Beamer Overlays and Animations

## Overview

Beamer's overlay system allows you to create dynamic presentations where content appears, disappears, or changes across multiple "slides" (overlays) within a single frame. This enables progressive disclosure, highlighting, and smooth information flow.

## Basic Concepts

### Overlay Specifications

Overlay specifications use angle brackets: `<n>` or `<n-m>` or `<n->`

| Specification | Meaning |
|---------------|---------|
| `<1>` | Only on overlay 1 |
| `<1-3>` | On overlays 1, 2, and 3 |
| `<2->` | From overlay 2 onwards |
| `<1-| alert@2>` | From 1 onwards, alert on 2 |

### Multiple Overlays

A frame with overlays creates multiple slides. Navigate with arrow keys or mouse clicks.

## Pause Command

### Simple Pause

```latex
\begin{frame}{Sequential Reveal}
  First point
  \pause
  Second point
  \pause
  Third point
\end{frame}
```

Creates 3 overlays: first point alone, then first+second, then all three.

### Pause in Lists

```latex
\begin{itemize}
  \item First point
  \pause
  \item Second point
  \pause
  \item Third point
\end{itemize}
```

## Overlay Specifications

### Itemize with Overlays

**Manual specification**:
```latex
\begin{itemize}
  \item<1-> Appears on slide 1 and stays
  \item<2-> Appears on slide 2 and stays
  \item<3-> Appears on slide 3 and stays
\end{itemize}
```

**Automatic sequential**:
```latex
\begin{itemize}[<+->]
  \item First point
  \item Second point
  \item Third point
\end{itemize}
```

The `[<+->]` option automatically increments overlay numbers.

### Enumerate with Overlays

```latex
\begin{enumerate}[<+->]
  \item First item
  \item Second item
  \item Third item
\end{enumerate}
```

### Mixed Overlays

```latex
\begin{itemize}
  \item<1-> Always visible
  \item<2-4> Only on slides 2-4
  \item<5-> From slide 5 onwards
\end{itemize}
```

## Only, Uncover, Visible

### Only

```latex
\only<1>{Only visible on slide 1}
\only<2>{Only visible on slide 2}
\only<3>{Only visible on slide 3}
```

**Behavior**: Content doesn't reserve space when hidden.

### Uncover

```latex
\uncover<2->{Appears on slide 2 and stays}
```

**Behavior**: Content reserves space but is invisible until shown.

### Visible

```latex
\visible<3->{Also appears on slide 3, reserves space}
```

**Behavior**: Similar to uncover, but space always reserved.

### Comparison

```latex
\begin{frame}{Comparison}
  \only<1>{Only: No space reserved}
  \uncover<2>{Uncover: Space reserved, invisible}
  \visible<3>{Visible: Space reserved, invisible}
\end{frame}
```

## Highlighting

### Alert on Specific Slide

```latex
\begin{itemize}
  \item Normal text
  \item<2| alert@2> Highlighted on slide 2
  \item Normal text
\end{itemize}
```

### Alert Block

```latex
\begin{alertblock}<2>{Important}
  This block appears on slide 2
\end{alertblock}
```

### Color Changes

```latex
\textcolor<2>{red}{This text turns red on slide 2}
```

## Overlays in Figures

### Sequential Figures

```latex
\begin{frame}{Building a Diagram}
  \includegraphics<1>[width=0.8\textwidth]{step1.png}
  \includegraphics<2>[width=0.8\textwidth]{step2.png}
  \includegraphics<3>[width=0.8\textwidth]{step3.png}
\end{frame}
```

### Overlay in TikZ

```latex
\begin{tikzpicture}
  % Base (always visible)
  \draw (0,0) rectangle (4,3);
  
  % Add on slide 2+
  \draw<2-> (1,1) circle (0.5);
  
  % Add on slide 3+
  \draw<3->[->, thick] (2,1.5) -- (3,2);
  
  % Highlight on slide 4
  \node<4>[red,thick] at (2,1.5) {Result};
\end{tikzpicture}
```

## Overlays in Tables

### Revealing Rows

```latex
\begin{table}
  \begin{tabular}{lcc}
    \toprule
    Method & Accuracy & Time \\
    \midrule
    Baseline & 0.82 & 10s \\
    \only<2->{Proposed & 0.94 & 15s \\}
    \only<3->{Best & 0.98 & 20s \\}
    \bottomrule
  \end{tabular}
\end{table}
```

### Highlighting Cells

```latex
\begin{table}
  \begin{tabular}{lcc}
    \toprule
    Method & Accuracy & Time \\
    \midrule
    Baseline & 0.82 & 10s \\
    Proposed & \only<1>{0.94}\only<2>{\textcolor{red}{\textbf{0.94}}} & 15s \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Overlays in Blocks

### Sequential Blocks

```latex
\begin{block}<1>{First Block}
  Content appears first
\end{block}

\begin{block}<2>{Second Block}
  Content appears second
\end{block}

\begin{alertblock}<3>{Third Block}
  Alert block appears last
\end{alertblock}
```

## Advanced Techniques

### Overlay-Aware Commands

```latex
\newcommand{\highlight}[1]{\textcolor<#1>{red}{\textbf{Important}}}
```

Usage:
```latex
\highlight{2}  % Highlights on slide 2
```

### Conditional Content

```latex
\only<1-2>{Early content}
\only<3->{Later content}
```

### Overlay Arithmetic

```latex
\only<+->{Next slide}
\only<+(1)->{Two slides ahead}
```

### Frame Counter

```latex
\only<1>{\frametitle{Introduction}}
\only<2>{\frametitle{Methods}}
\only<3>{\frametitle{Results}}
```

## Best Practices

### Do

✅ Use overlays for progressive disclosure
✅ Keep overlay logic simple
✅ Test navigation (arrow keys, clicks)
✅ Use consistent overlay patterns
✅ Reserve space appropriately (uncover vs only)

### Don't

❌ Create too many overlays (max 5-6 per frame)
❌ Mix overlay styles inconsistently
❌ Use overlays unnecessarily
❌ Forget to test on actual presentation computer
❌ Create confusing sequences

## Common Patterns

### Three-Point Reveal

```latex
\begin{frame}{Three Points}
  \begin{itemize}[<+->]
    \item Point 1
    \item Point 2
    \item Point 3
  \end{itemize}
\end{frame}
```

### Problem-Solution

```latex
\begin{frame}{Problem and Solution}
  \begin{block}<1>{Problem}
    Description of the problem
  \end{block}
  
  \begin{block}<2>{Solution}
    Our approach to solving it
  \end{block}
\end{frame}
```

### Before-After Comparison

```latex
\begin{frame}{Comparison}
  \begin{columns}
    \begin{column}{0.5\textwidth}
      \textbf{Before}
      \includegraphics<1>[width=\textwidth]{before.png}
    \end{column}
    \begin{column}{0.5\textwidth}
      \textbf{After}
      \includegraphics<2>[width=\textwidth]{after.png}
    \end{column}
  \end{columns}
\end{frame}
```

### Building a Diagram

```latex
\begin{frame}{Process}
  \begin{tikzpicture}
    \node<1-> (start) {Start};
    \node<2->[right=of start] (step1) {Step 1};
    \node<3->[right=of step1] (step2) {Step 2};
    \node<4->[right=of step2] (end) {End};
    
    \draw<2->[->] (start) -- (step1);
    \draw<3->[->] (step1) -- (step2);
    \draw<4->[->] (step2) -- (end);
  \end{tikzpicture}
\end{frame}
```

## Troubleshooting

### Overlays Not Working

**Problem**: Content doesn't appear/disappear
**Solution**: Check syntax `<n>` vs `<n->`, ensure proper spacing

### Too Many Slides

**Problem**: Frame creates too many overlays
**Solution**: Review overlay specifications, simplify logic

### Navigation Issues

**Problem**: Can't navigate overlays
**Solution**: Use arrow keys or mouse clicks, check PDF viewer supports overlays

### Space Issues

**Problem**: Layout shifts between overlays
**Solution**: Use `\uncover` instead of `\only` to reserve space

## Summary

Overlays enable:
- Progressive disclosure
- Highlighting key points
- Building complex diagrams
- Smooth information flow

Use overlays strategically to enhance understanding, not just for visual effect.
