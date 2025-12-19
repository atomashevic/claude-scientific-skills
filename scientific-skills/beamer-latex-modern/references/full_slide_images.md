# Full-Slide Images in Modern Beamer

## Overview

Full-slide images are a powerful technique for creating visually impactful slides where the image occupies the entire slide area, bypassing Beamer's default margins and decorations. This is achieved using TikZ overlays.

## The FullSlideImage Command

### Definition

```latex
\newcommand{\FullSlideImage}[1]{%
  \begin{frame}[plain]
    \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=center] at (current page.center) {%
        \includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{#1}%
      };
    \end{tikzpicture}
  \end{frame}
}
```

### Usage

```latex
% Single image slide
\FullSlideImage{figures/methodology.png}

% Multiple image slides in sequence
\FullSlideImage{figures/slide01.png}
\FullSlideImage{figures/slide02.png}
\FullSlideImage{figures/slide03.png}
```

## How It Works

### Key Components

1. **`[plain]` frame option**: Removes all Beamer decorations (headers, footers, navigation)

2. **`remember picture`**: Allows TikZ to reference the page coordinate system across compilations

3. **`overlay`**: Places the TikZ content on top of everything, ignoring normal layout

4. **`current page.center`**: References the exact center of the physical page

5. **`keepaspectratio`**: Maintains image proportions, prevents distortion

### Why TikZ Overlay?

Standard `\includegraphics` within Beamer frames is subject to:
- Text margins (default 10mm or custom)
- Frame title space
- Header/footer space

The TikZ overlay bypasses all of these, placing the image directly on the page canvas.

## Image Preparation

### Resolution Requirements

For 16:9 aspect ratio (aspectratio=169):

| Quality | Dimensions | File Size |
|---------|------------|-----------|
| Minimum | 1920 × 1080 | ~1-3 MB |
| Good | 2560 × 1440 | ~2-5 MB |
| Excellent | 3840 × 2160 | ~5-10 MB |

### Aspect Ratio

**Match your Beamer aspect ratio**:
- `aspectratio=169` → 16:9 → 1.778:1
- `aspectratio=43` → 4:3 → 1.333:1
- `aspectratio=1610` → 16:10 → 1.6:1

If image ratio doesn't match, `keepaspectratio` will:
- Scale to fit the constraining dimension
- Leave white bars on the sides or top/bottom

### File Formats

| Format | Best For | Notes |
|--------|----------|-------|
| PNG | Diagrams, screenshots | Lossless, larger files |
| PDF | Vector graphics | Scalable, small files |
| JPG | Photographs | Lossy, smaller files |

**Recommendation**: Use PNG for slides with text/diagrams, PDF for vector content.

## Creating Full-Slide Images

### Using Presentation Software

Export slides from PowerPoint, Keynote, or Google Slides:

1. Create slide at 16:9 ratio
2. Design with all text, graphics, annotations
3. Export as PNG at high resolution
4. Use in Beamer with `\FullSlideImage`

### Using Python/Matplotlib

```python
import matplotlib.pyplot as plt

# Create figure at 16:9 aspect ratio
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)

# Your visualization code
ax.plot(x, y)
ax.set_title('Results', fontsize=24)

# Save
plt.savefig('figures/results.png', dpi=150, bbox_inches='tight')
```

### Using Scientific Schematics Skill

Generate publication-quality diagrams:

```bash
python scripts/generate_schematic.py "methodology flowchart showing data collection, preprocessing, analysis, and validation steps" -o figures/methodology.png
```

## Use Cases

### Title Slides

Create visually striking title slides with full control:

```latex
% Title slide as image (recommended)
\FullSlideImage{figures/title_slide.png}

% Contains:
% - Title text
% - Author name
% - Institution
% - Conference/date
% - Optional background image
```

### Methodology Diagrams

Complex flowcharts work better as complete images:

```latex
% Research pipeline visualization
\FullSlideImage{figures/pipeline.png}
```

### Key Results

Maximum visual impact for important findings:

```latex
% Full-slide chart or visualization
\FullSlideImage{figures/main_result.png}
```

### Transition Slides

Section dividers with visual interest:

```latex
% Section intro slide
\FullSlideImage{figures/section_methods.png}
```

## Mixing with Regular Slides

### Typical Pattern

```latex
% Title (image)
\FullSlideImage{figures/title.png}

% Motivation (text)
\begin{frame}{Motivation}
\begin{enumerate}
  \item Point 1
  \item Point 2
\end{enumerate}
\end{frame}

% Background diagram (image)
\FullSlideImage{figures/background.png}

% Methods (text)
\begin{frame}{Methods}
...
\end{frame}

% Pipeline (image)
\FullSlideImage{figures/pipeline.png}

% Results table (text)
\begin{frame}{Results}
...
\end{frame}

% Results chart (image)
\FullSlideImage{figures/results_chart.png}
```

### Balance Recommendations

- **Conference talk (15 min)**: 30-50% image slides
- **Seminar (45 min)**: 20-40% image slides
- **Thesis defense (60 min)**: 20-30% image slides

## Advanced Techniques

### Image with Caption Overlay

Add a caption on top of the image:

```latex
\begin{frame}[plain]
  \begin{tikzpicture}[remember picture,overlay]
    % Image
    \node[anchor=center] at (current page.center) {%
      \includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{figure.png}%
    };
    % Caption at bottom
    \node[anchor=south,fill=white,fill opacity=0.8,text opacity=1] 
      at (current page.south) {%
        \footnotesize Figure 1: Description of the visualization
      };
  \end{tikzpicture}
\end{frame}
```

### Multiple Images on One Slide

```latex
\begin{frame}[plain]
  \begin{tikzpicture}[remember picture,overlay]
    % Left image
    \node[anchor=west] at ([xshift=5mm]current page.west) {%
      \includegraphics[width=0.48\paperwidth]{fig1.png}%
    };
    % Right image
    \node[anchor=east] at ([xshift=-5mm]current page.east) {%
      \includegraphics[width=0.48\paperwidth]{fig2.png}%
    };
  \end{tikzpicture}
\end{frame}
```

### Fade Effect Between Images

For PDF viewers that support transitions:

```latex
\FullSlideImage{figures/before.png}
\FullSlideImage{figures/after.png}  % Quick manual flip
```

## Troubleshooting

### Image Doesn't Fill Slide

**Cause**: Image aspect ratio doesn't match slide ratio.

**Solution**: 
- Create image at exact 16:9 ratio
- Or accept white bars with `keepaspectratio`
- Or use `width=\paperwidth,height=\paperheight` without `keepaspectratio` (may distort)

### Image Appears Behind Other Content

**Cause**: `overlay` not working correctly.

**Solution**: Ensure `\FullSlideImage` creates its own frame, not mixed with other content.

### Compilation Slow

**Cause**: Large image files.

**Solution**:
- Compress images before including
- Use appropriate resolution (1920×1080 is usually sufficient)
- Use `draft` mode during development: `\documentclass[draft]{beamer}`

### TikZ Errors

**Cause**: Missing TikZ libraries or incorrect syntax.

**Solution**: Ensure preamble includes:
```latex
\usepackage{tikz}
\usetikzlibrary{calc}
```

## Best Practices

### Do

✅ Create images at the correct aspect ratio
✅ Include all text/labels in the image for full control
✅ Maintain consistent visual style across all image slides
✅ Use high resolution for clarity
✅ Test on actual projector if possible

### Don't

❌ Mix `\FullSlideImage` content with regular frame content
❌ Use low-resolution images (pixelation is obvious)
❌ Forget to update images when content changes
❌ Over-rely on image slides (balance with text slides)
❌ Use inconsistent fonts between image and text slides

## File Organization

Recommended structure:

```
presentation/
├── main.tex
├── references.bib
└── figures/
    ├── title_slide.png
    ├── methodology.png
    ├── pipeline.png
    ├── results_1.png
    ├── results_2.png
    └── conclusions.png
```

Use consistent naming:
- `slide01_title.png`
- `slide03_background.png`
- `slide08_results.png`

This makes reordering and updating easier.
