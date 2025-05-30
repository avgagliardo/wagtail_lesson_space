from wagtail import blocks

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
