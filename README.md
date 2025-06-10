
# Wagtail Lesson Space

Wagtail Lesson Space is a modular, test-driven Wagtail CMS project designed to support educational content repositories. It includes a reusable StreamField block system, a fully customizable homepage, and support for lessons with rich content features.

## Features

- Custom homepage powered by a StreamField block editor
- Lesson pages with subtitle and tag support
- Reusable block library (`porpoise_blocks`) with essential content blocks
- Code block with syntax highlighting, line numbering, dark mode toggle, and copy-to-clipboard
- Static files (CSS/JS) managed through `static/` and integrated via base templates
- Test suite covering templates, static assets, and rendering logic
- Environment managed using `pyenv`

## Requirements

- Python 3.8+ (recommended via pyenv)
- pip and virtualenv
- PostgreSQL or SQLite (for development)
- Node.js (optional, for asset pipeline expansion)

## Installation

Clone the repository and configure the environment:

```bash
git clone https://github.com/avgagliardo/wagtail_lesson_space.git
cd wagtail_lesson_space
```

Install the correct Python version using pyenv:

```bash
pyenv install 3.8.10
pyenv local 3.8.10
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Access the admin interface at http://localhost:8000/admin.


## Static Media Installation (may be necessary):
### 1. **Create Missing Static Paths**

The following static directories were not present and were added:

```
lesson_space/static/css/
lesson_space/static/js/
```

---

### 2. **Add Referenced Files**

Missing files referenced by `{% static %}` in templates were created with placeholder content:

| File Path                           | Type | Contents                              |
|------------------------------------|------|----------------------------------------|
| `lesson_space/static/css/lesson_space.css` | CSS  | `body { font-family: sans-serif; }`    |
| `lesson_space/static/css/welcome_page.css` | CSS  | `body.welcome { background: white; }`  |
| `lesson_space/static/js/lesson_space.js`   | JS   | `console.log("lesson space loaded");`  |

---

### 3. **Reset Staticfiles Manifest**

The previous static files output directory and manifest were cleared:

```bash
rm -rf static/
python manage.py collectstatic --noinput
```

This ensured all referenced assets were hashed and collected properly.

---

### 4. **Test Verification**

The following test suite was used to verify fixes:

```bash
pytest home
```

Errors related to static asset resolution were eliminated once files were added and `collectstatic` was re-run.



---

## 📜 Automation Script

A shell script (`patch_static_files.sh`) was created to automate the above steps. It is documented in `README.md`.

---

## 📝 Final Notes

- **ManifestStaticFilesStorage is strict**: all files referenced via `{% static %}` must exist on disk and be included in `STATICFILES_DIRS`
- Ensure changes to templates that add new static assets are always followed by file creation and `collectstatic`
- This patch unblocks fresh installs and CI runs that previously failed on rendering tests




















## Block System

All reusable StreamField blocks are implemented in the `porpoise_blocks` app. This block library is modular and supports the following categories:

- `text_blocks`: includes `HeadingBlock`, `ParagraphBlock`, `CalloutBlock`, `QuoteBlock`, `CodeBlock`
- `media_blocks`: support for images, files, and media embeds (planned)
- `math_blocks`: blocks for LaTeX or KaTeX content (optional)
- `layout_blocks` and `interactive_blocks`: reserved for advanced UI features (optional)

The default StreamField composition is defined using `ESSENTIAL_BLOCKS` in `porpoise_blocks.common`:

```python
ESSENTIAL_BLOCKS = [
    ("heading", HeadingBlock()),
    ("paragraph", ParagraphBlock()),
    ("callout", CalloutBlock()),
    ("quote", QuoteBlock()),
    ("code", CodeBlock()),
]
```

Each block has an associated template in `porpoise_blocks/templates/blocks/`.

## Homepage Customization

The homepage is implemented via a custom `HomePage` model defined in `home/models.py`. It uses a StreamField to allow arbitrary composition of essential content blocks via the admin interface.

Template path: `home/templates/home/home_page.html`

Modifications to the homepage structure should be made by editing:

- `HomePage` model fields and panels
- `home_page.html` template for layout/rendering
- `porpoise_blocks` for changes to available block types

## Lesson Pages

The `LessonPage` model extends Wagtail’s `Page` class and includes:

- Subtitle field (`CharField`)
- Tagging via `ClusterTaggableManager`
- StreamField for lesson content using `ESSENTIAL_BLOCKS`

Tags are managed using the `LessonPageTag` model (a subclass of `TaggedItemBase`).

## Static Assets

All CSS and JavaScript assets are stored in the `static/` directory and served under `/static/`.

Key static assets:

- `static/css/lesson_space.css`: core styles
- `static/js/lesson_space.js`: handles code block controls

Static file tests are located in `home/tests/test_static.py`.

## Testing

Run the full test suite using:

```bash
pytest
```

Tests cover:

- Static file resolution
- Block rendering in templates
- Page model integration
- Homepage and LessonPage behaviors

Test directories:

- `home/tests/`
- `porpoise_blocks/tests/`

## Project Structure

```
wagtail_lesson_space/
├── home/                   # Homepage and lesson page logic
├── porpoise_blocks/        # Reusable StreamField blocks
├── search/                 # Placeholder for future search config
├── static/                 # JavaScript, CSS, assets
├── templates/              # Global and app-specific templates
├── Dockerfile              # Optional container support
├── manage.py
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
