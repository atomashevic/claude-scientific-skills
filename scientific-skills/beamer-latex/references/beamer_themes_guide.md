# Beamer Themes Guide

## Overview

Beamer themes control the overall visual appearance of your presentation. Themes are modular: you combine a **presentation theme** (layout), **color theme** (colors), and **font theme** (typography) to create your desired look.

## Presentation Themes

Presentation themes control the structural layout, navigation, and overall design.

### Classic Themes

**Madrid**:
```latex
\usetheme{Madrid}
```
- Rounded blocks with shadows
- Navigation dots in header
- Professional, modern appearance
- Good for: Academic conferences, seminars

**Berlin**:
```latex
\usetheme{Berlin}
```
- Section navigation in header
- Sidebar navigation
- Structured, organized
- Good for: Long presentations, thesis defenses

**Copenhagen**:
```latex
\usetheme{Copenhagen}
```
- Minimal, clean design
- Simple navigation
- Uncluttered appearance
- Good for: Modern talks, technical presentations

**Boadilla**:
```latex
\usetheme{Boadilla}
```
- Simple footer with frame numbers
- Clean, traditional
- Good for: Professional presentations

**Pittsburgh**:
```latex
\usetheme{Pittsburgh}
```
- Very minimal
- Frame numbers only
- Maximum content space
- Good for: Content-heavy presentations

### Modern Themes

**CambridgeUS**:
```latex
\usetheme{CambridgeUS}
```
- Blue gradient backgrounds
- Modern, polished
- Good for: Corporate, professional

**Singapore**:
```latex
\usetheme{Singapore}
```
- Minimalist Asian style
- Clean lines
- Good for: Modern academic talks

**Rochester**:
```latex
\usetheme{Rochester}
```
- Extremely minimal
- Frame titles only
- Good for: Maximum simplicity

**Antibes**:
```latex
\usetheme{Antibes}
```
- Tree-style navigation
- Unique appearance
- Good for: Distinctive presentations

### Navigation-Heavy Themes

**AnnArbor**:
```latex
\usetheme{AnnArbor}
```
- Vertical section navigation
- Good for: Structured talks with many sections

**Bergen**:
```latex
\usetheme{Bergen}
```
- Side navigation panel
- Good for: Long presentations

**Berkeley**:
```latex
\usetheme{Berkeley}
```
- Left sidebar navigation
- Good for: Hierarchical content

**Goettingen**:
```latex
\usetheme{Goettingen}
```
- Right sidebar navigation
- Good for: Structured content

### Default Theme

**default**:
```latex
\usetheme{default}
```
- Minimal, no decorations
- Maximum customization freedom
- Good for: Custom designs

## Color Themes

Color themes apply color schemes to any presentation theme.

### Cool Colors

**default** (Blue):
```latex
\usecolortheme{default}
```
- Classic Beamer blue
- Professional, safe choice

**dolphin**:
```latex
\usecolortheme{dolphin}
```
- Cyan-blue tones
- Modern, fresh

**whale**:
```latex
\usecolortheme{whale}
```
- Dark blue with accents
- Professional, serious

**seagull**:
```latex
\usecolortheme{seagull}
```
- Grayscale
- Neutral, professional

### Warm Colors

**beaver**:
```latex
\usecolortheme{beaver}
```
- Red/brown tones
- Warm, academic

**rose**:
```latex
\usecolortheme{rose}
```
- Pink/red tones
- Soft, approachable

**crane**:
```latex
\usecolortheme{crane}
```
- Orange/yellow tones
- Energetic, vibrant

### Nature Colors

**orchid**:
```latex
\usecolortheme{orchid}
```
- Purple tones
- Distinctive, creative

**lily**:
```latex
\usecolortheme{lily}
```
- Light, pastel colors
- Soft, gentle

**spruce**:
```latex
\usecolortheme{spruce}
```
- Green tones
- Natural, calm

## Font Themes

Font themes control typography.

**default**:
```latex
\usefonttheme{default}
```
- Standard Beamer fonts
- Sans-serif for structure

**serif**:
```latex
\usefonttheme{serif}
```
- Serif fonts throughout
- Traditional, academic

**structurebold**:
```latex
\usefonttheme{structurebold}
```
- Bold structure elements
- Strong emphasis

**structureitalicserif**:
```latex
\usefonttheme{structureitalicserif}
```
- Italic serif structure
- Elegant, formal

**professionalfonts**:
```latex
\usefonttheme{professionalfonts}
```
- Don't modify math fonts
- Preserve LaTeX math appearance

## Popular Theme Combinations

### Professional Academic

```latex
\usetheme{Madrid}
\usecolortheme{default}
\usefonttheme{default}
```
- Classic, professional
- Safe for any academic context

### Warm Academic

```latex
\usetheme{Madrid}
\usecolortheme{beaver}
\usefonttheme{default}
```
- Warm, approachable
- Good for humanities, social sciences

### Minimal Modern

```latex
\usetheme{Copenhagen}
\usecolortheme{seagull}
\usefonttheme{default}
```
- Clean, minimal
- Maximum content focus

### Corporate Professional

```latex
\usetheme{Boadilla}
\usecolortheme{orchid}
\usefonttheme{structurebold}
```
- Distinctive, professional
- Good for business presentations

### Technical/Engineering

```latex
\usetheme{Berlin}
\usecolortheme{dolphin}
\usefonttheme{default}
```
- Structured, technical
- Good for engineering, CS

## Custom Colors

Define and apply custom colors:

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
\setbeamercolor{item}{fg=myblue}
```

### Color Elements

| Element | Description |
|---------|-------------|
| `structure` | Overall structure color |
| `title` | Title slide text |
| `frametitle` | Frame title text and background |
| `block title` | Block title text and background |
| `block body` | Block body text and background |
| `item` | Bullet point color |
| `normal text` | Body text color |
| `background canvas` | Slide background |

## Customizing Themes

### Remove Navigation Symbols

```latex
\setbeamertemplate{navigation symbols}{}
```

### Custom Footer

```latex
% Frame numbers only
\setbeamertemplate{footline}[frame number]

% Custom footer
\setbeamertemplate{footline}{
  \hfill\insertframenumber/\inserttotalframenumber\hspace{2mm}\vspace{2mm}
}
```

### Custom Frame Title

```latex
\setbeamertemplate{frametitle}{%
  \vspace*{0.5em}%
  {\Large\bfseries\insertframetitle\par}%
  \vspace*{0.3em}%
}
```

### Custom Blocks

```latex
% Rounded blocks without shadow
\setbeamertemplate{blocks}[rounded][shadow=false]

% Default blocks
\setbeamertemplate{blocks}[default]
```

## Theme Selection Guide

### For Academic Conferences

**Recommended**: Madrid + default/beaver
- Professional appearance
- Good visibility
- Familiar to academic audiences

### For Seminars

**Recommended**: Berlin + default/dolphin
- Section navigation helpful
- Structured appearance
- Good for longer talks

### For Thesis Defenses

**Recommended**: Berlin + default
- Formal, structured
- Clear navigation
- Professional appearance

### For Corporate/Business

**Recommended**: Boadilla/CambridgeUS + orchid/default
- Clean, professional
- Distinctive but not distracting
- Business-appropriate

### For Technical Talks

**Recommended**: Copenhagen + seagull/dolphin
- Minimal distractions
- Focus on content
- Modern appearance

## Best Practices

### Consistency

- Use the same theme throughout
- Don't mix themes mid-presentation
- Maintain consistent colors

### Readability

- Ensure sufficient contrast
- Test on actual projector
- Consider colorblind accessibility

### Appropriateness

- Match theme to audience
- Consider institutional preferences
- Align with presentation context

## Troubleshooting

### Theme Not Loading

**Problem**: Theme not found
**Solution**: Ensure Beamer is fully installed:
```bash
tlmgr install beamer
```

### Colors Not Applying

**Problem**: Custom colors don't appear
**Solution**: Load `xcolor` package:
```latex
\usepackage{xcolor}
```

### Navigation Issues

**Problem**: Navigation symbols appear when unwanted
**Solution**: Explicitly remove:
```latex
\setbeamertemplate{navigation symbols}{}
```

## Summary

Choose themes based on:
1. **Presentation type**: Conference, seminar, defense, corporate
2. **Content structure**: Many sections → Berlin, simple → Copenhagen
3. **Audience**: Academic → Madrid/Berlin, Business → Boadilla/CambridgeUS
4. **Personal preference**: Test combinations, find what works

Remember: The best theme is one that doesn't distract from your content.
