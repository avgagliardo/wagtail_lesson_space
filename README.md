# Lesson Space

Welcome to the Wagtail Lesson Space project. This is a Wagtail-based platform designed for educational publishing. It supports LaTeX rendering, modular StreamField blocks, PDF embedding, and flexible page structures tailored for knowledge repositories.


---

## 📚 Project Documentation

| Section                                      | Description                                      |
|---------------------------------------------|--------------------------------------------------|
| [▶️ Overview](#️project-overview)             | Project goals, architecture, and features       |
| [▶️ Installation & Static File Setup](#️installation--static-file-setup) | Setup guide, static patching, collectstatic     |
| [▶️ LaTeX Rendering (KaTeX)](#️latex-rendering-katex) | Guide to writing and rendering math in LaTeX    |
| [▶️ Available StreamField Blocks](#️available-streamfield-blocks) | Summary of reusable block types                 |
| [▶️ Homepage Customization](#️homepage-customization) | Explanation of the modified homepage and layout |

---

<details>
<summary id="️project-overview"><strong>🧠 Project Overview</strong></summary>

<br>


This section provides an overview of the Lesson Space project's architecture and goals.
- Wagtail CMS foundation
- Modular block definitions in `porpoise_blocks`
- Clean reverse-proxy readiness for NGINX
- Python environment bootstrapped with `pyenv`


</details>


<details>
<summary id="️installation--static-file-setup"><strong>🛠️ Installation & Static File Setup</strong></summary>

<br>

## 🔧 Initial Setup (Local Dev)

Clone the repository and enter the project directory:

```bash
git clone https://github.com/avgagliardo/wagtail_lesson_space.git
cd wagtail_lesson_space
```

### 🐍 Python Environment (via `pyenv`)

```bash
pyenv install 3.11.8
pyenv virtualenv 3.11.8 wagtail-lessons-env
pyenv activate wagtail-lessons-env
pip install -r requirements.txt
```

### 🗂️ Static File Structure & Manifest Setup

This project uses `ManifestStaticFilesStorage`, which requires all referenced static assets to:

- Exist on disk
- Be properly collected into a hashed manifest
- Match `{% static %}` template references

Run the provided setup script:

```bash
bash patch_static_files.sh
```

This script:
- Creates required directories (`lesson_space/static/css`, `.../js`)
- Writes minimal placeholder content to:
  - `lesson_space.css`
  - `welcome_page.css`
  - `lesson_space.js`
- Runs `collectstatic` to generate the manifest

### ✅ Migrations & Superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 🧪 Run Tests

```bash
pytest
```

Tests in the `home` app verify:
- Static files are collected and served
- Homepage renders successfully
- `LessonPage` logic and URLs behave as expected

</details>




<details>
<summary id="️latex-rendering-katex"><strong>📐 LaTeX Rendering (KaTeX)</strong></summary>

<br>

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

</details>


<details>
<summary id="️available-streamfield-blocks"><strong>🧱 Available StreamField Blocks</strong></summary>

<br>


A curated set of blocks are implemented in `porpoise_blocks/`:
- `QuoteBlock`: Styled pull-quotes with optional metadata
- `CodeBlock`: Syntax-highlighted code with copy/dark mode
- `LaTeXBlock`: Rendered math via KaTeX
- Additional planned: image annotation, list blocks with interactivity


</details>

<details>
<summary id="️homepage-customization"><strong>🖼️ Homepage Customization</strong></summary>

<br>


The homepage has been customized with:
- Custom `HomePage` model
- Clean static CSS served under `/static/css/lesson_space.css`
- Navigation-ready base layout using `base.html`
- Unit tests ensure static files and homepage render correctly


</details>