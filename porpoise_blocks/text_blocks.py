from wagtail import blocks
from wagtail.blocks import ChoiceBlock, RichTextBlock, CharBlock, StructBlock

# Heading Block (Extension)
class HeadingBlock(blocks.CharBlock):
    """
    A short heading block (e.g., section titles).
    
    - Inherits Wagtail's built-in CharBlock.
    - Useful for page sections, callouts, or inline headings.
    - Custom styling/templates can target this block type.
    """
    def __init__(self, *args, **kwargs):
        defaults = {
            "label": "Heading",
            "icon": "title",
            "help_text": "Short section heading or title text.",
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

    # Example of redefining the template later:
    # class HeadingBlock(...):
    #     class Meta:
    #         template = "blocks/heading_block.html"

# Paragraph Block (Extension)
class ParagraphBlock(blocks.RichTextBlock):
    """
    A rich text paragraph block for standard body content.

    - Restricts formatting features to ensure editorial consistency.
    - Can be extended with validation, custom rendering, or templates.
    """
    def __init__(self, *args, **kwargs):
        defaults = {
            "label": "Paragraph",
            "icon": "pilcrow",
            "features": ["bold", "italic", "link", "ul", "ol", "code"],
            "help_text": "Rich text content block with limited formatting.",
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

    # Example validator extension:
    # def clean(self, value):
    #     if len(value) > 100:
    #         raise ValidationError("Heading too long.")
    #     return super().clean(value)

# Callout Block
class CalloutBlock(StructBlock):
    title = CharBlock(required=False, help_text="Optional short heading")
    body = RichTextBlock(features=["bold", "italic", "link", "ul", "ol"])
    style = ChoiceBlock(choices=[], help_text="Visual style")  # empty for now

    def __init__(self, *args, **kwargs):
        styles = kwargs.pop("styles", [
            ("info", "Info"),
            ("warning", "Warning"),
            ("success", "Success"),
            ("danger", "Danger"),
            ("note", "Note"),
        ])
        super().__init__(*args, **kwargs)

        # Set the choices dynamically
        self.child_blocks["style"].choices = styles

        # ✅ Rebind field to reflect the new choices in the admin
        self.child_blocks["style"].field = ChoiceBlock(choices=styles).field

    class Meta:
        template = "porpoise_blocks/callout_block.html"
        icon = "placeholder"
        label = "Callout"
        help_text = "Stylized box for warnings, tips, notes, etc."




























# Quote Block
class QuoteBlock(blocks.StructBlock):
    quote = blocks.RichTextBlock(
        features=["bold", "italic", "link"],
        label="Quote",
        help_text="The main quoted text."
    )
    attribution = blocks.CharBlock(
        required=False,
        label="Attribution",
        help_text="Who said it (optional)."
    )
    style = blocks.ChoiceBlock(
        choices=[
            ("default", "Default"),
            ("highlight", "Highlighted"),
            ("bordered", "Bordered"),
        ],
        default="default",
        required=False,
        label="Style",
        help_text="Visual style of the quote block."
    )

    class Meta:
        icon = "openquote"
        label = "Quote"
        template = "porpoise_blocks/quote_block.html"


# Code Block
class CodeBlock(blocks.StructBlock):
    language = blocks.ChoiceBlock(
        choices=[
            ("text", "Plain Text"),
            ("python", "Python"),
            ("bash", "Bash"),
            ("json", "JSON"),
            ("html", "HTML"),
            ("javascript", "JavaScript"),
        ],
        default="text",
        label="Language",
        help_text="Programming language for syntax highlighting."
    )
    code = blocks.TextBlock(
        label="Code",
        help_text="The source code block."
    )
    caption = blocks.CharBlock(
        required=False,
        label="Caption",
        help_text="Optional filename or note."
    )
    style = blocks.ChoiceBlock(
        choices=[
            ("default", "Default"),
            ("box", "Boxed"),
            ("lined", "Box + Line Numbers"),
        ],
        default="default",
        required=False,
        label="Style",
        help_text="Visual style of the code block."
    )
    
    class Meta:
        icon = "code"
        label = "Code"
        template = "porpoise_blocks/code_block.html"

