# Mathematical Typesetting Reference

Complete reference for mathematical notation in LaTeX.

## Math Modes

### Inline Math
```latex
The equation $E = mc^2$ is famous.
```

### Display Math
```latex
\begin{equation}
  E = mc^2
  \label{eq:einstein}
\end{equation}
```

## Greek Letters

### Lowercase
```latex
\alpha \beta \gamma \delta \epsilon \zeta \eta \theta
\iota \kappa \lambda \mu \nu \xi \pi \rho \sigma \tau
\upsilon \phi \chi \psi \omega
```

### Uppercase
```latex
\Gamma \Delta \Theta \Lambda \Xi \Pi \Sigma
\Upsilon \Phi \Psi \Omega
```

## Subscripts and Superscripts

```latex
x^2              % Superscript
x_1               % Subscript
x^{2+3}           % Complex superscript
x_{i,j}           % Complex subscript
```

## Fractions and Roots

```latex
\frac{a}{b}       % Standard fraction
\sqrt{x}          % Square root
\sqrt[n]{x}        % nth root
```

## Sums, Products, Integrals

```latex
\sum_{i=1}^{n}     % Summation
\prod_{i=1}^{n}    % Product
\int_{0}^{\infty}  % Integral
```

## Common Mathematical Expressions

### Probability
```latex
P(A \mid B)     % Conditional probability
\mathbb{P}(A)   % Probability measure
E[X]            % Expected value
```

### Linear Algebra
```latex
\mathbf{A}      % Matrix
\mathbf{x}      % Vector
\det(\mathbf{A}) % Determinant
```

### Calculus
```latex
\frac{\partial f}{\partial x}  % Partial derivative
\frac{d f}{d x}                % Total derivative
\nabla f                        % Gradient
```

## Matrices

```latex
\begin{pmatrix} a & b \\ c & d \end{pmatrix}
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{vmatrix} a & b \\ c & d \end{vmatrix}
```

## Aligned Equations

```latex
\begin{align}
  x &= a + b \\
  y &= c + d
\end{align}
```
