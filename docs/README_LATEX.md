
# Wagtail LaTeX Rendering (KaTeX)

This project supports client-side LaTeX rendering via [KaTeX](https://katex.org/), one of the fastest and most widely-used math typesetting libraries for the web. All mathematical content inside LaTeX blocks is rendered dynamically in the browser using JavaScript.

---

## 🧠 How It Works

- The `LaTeXBlock` is implemented as a custom Wagtail `TextBlock` subclass (located in `porpoise_blocks/latex_codes.py`).
- The content entered into this block is inserted into the HTML frontend template (`porpoise_blocks/templates/porpoise_blocks/latex_block.html`).
- Rendering is handled by **KaTeX**, which is loaded via CDN in the base HTML template (`base.html` or equivalent).
- KaTeX automatically scans the DOM and replaces matching LaTeX expressions with fully rendered math.

---

## ✅ LaTeX Syntax Supported

KaTeX supports a large subset of LaTeX, including:

### Display Math
Use double dollar signs (`$$`) to indicate display math:
```latex
$$
\int_a^b f(x) \, dx = F(b) - F(a)
$$
```

### Inline Math
Use `\(...\)` for inline math:
```latex
The solution is \(x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\).
```

### Environments
KaTeX supports environments like `\begin{matrix}`, `\begin{aligned}`, etc., e.g.:

```latex
\begin{aligned}
a^2 + b^2 &= c^2 \\
e^{i\pi} + 1 &= 0
\end{aligned}
```

---

## 🚫 Limitations

- **No custom macros** (unless explicitly configured).
- **No TikZ**, **no PGFPlots** — graphical LaTeX packages are not supported.
- **Some rare symbols** or packages may not be available.

---

## 📚 Official Documentation

For full reference and advanced syntax, consult:

- 📘 **KaTeX Docs**: [https://katex.org/docs/supported.html](https://katex.org/docs/supported.html)
- 📘 **Function Support List**: [https://katex.org/docs/supported.html#functions](https://katex.org/docs/supported.html#functions)
- 📘 **Auto-render extension** (used in this project): [https://katex.org/docs/autorender.html](https://katex.org/docs/autorender.html)
- 📘 **LaTeX-to-KaTeX Compatibility Table**: [https://katex.org/docs/support_table.html](https://katex.org/docs/support_table.html)

---

## 🛠️ How to Add LaTeX

1. In the Wagtail editor, select the **LaTeX block**.
2. Enter math syntax using `$$...$$` for block math or `\(...\)` for inline.
3. Save and publish — rendering happens automatically in the frontend.

---

## 📂 Relevant Files

- **Block Definition**: `porpoise_blocks/latex_codes.py`
- **Frontend Template**: `porpoise_blocks/templates/porpoise_blocks/latex_block.html`
- **KaTeX CDN Injection**: `base.html` (or wherever layout HTML is defined)
- **Wagtail StreamField Use**: Typically added in `common.py` or your page model.

---

## 💬 Feedback and Contribution

KaTeX is under active development — if something doesn’t render as expected, check:
- Console for rendering errors
- KaTeX docs for function support

Feature requests or bug reports for this Wagtail integration can be submitted via the project issue tracker.
