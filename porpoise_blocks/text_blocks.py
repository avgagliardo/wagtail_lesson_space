from wagtail import blocks
from wagtail.blocks import ChoiceBlock, RichTextBlock, CharBlock, StructBlock

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


























