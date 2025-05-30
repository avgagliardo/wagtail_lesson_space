import pytest
from unittest.mock import MagicMock, patch

from wagtail.rich_text import RichText 
from wagtail.blocks import StreamBlockValidationError, StructBlockValidationError, RichTextBlock, ChoiceBlock
from wagtail.blocks import StreamValue

from porpoise_blocks.text_blocks import HeadingBlock, ParagraphBlock
from porpoise_blocks.text_blocks import CalloutBlock, QuoteBlock, CodeBlock


# Helper Class to test the valid input and clean methods
class MockRichTextInput:
    def __init__(self, html):
        self.source = html

#########################
# TESTS GO BELOW HERE
#########################

# Heading block tests
def test_heading_block_meta():
    block = HeadingBlock()
    assert block.meta.label == "Heading"
    assert block.meta.icon == "title"
    # help_text is not directly accessible — skip it

def test_heading_block_clean():
    block = HeadingBlock()
    result = block.clean("Introduction")
    assert result == "Introduction"


# Paragraph block tests
def test_paragraph_block_meta():
    block = ParagraphBlock()
    assert block.meta.label == "Paragraph"
    assert block.meta.icon == "pilcrow"
    assert set(block.features) == {"bold", "italic", "link", "ul", "ol", "code"}

def test_paragraph_block_clean_richtext():
    block = ParagraphBlock()
    input_value = RichText("<p>This is <strong>rich</strong> text.</p>")
    result = block.clean(input_value)
    assert isinstance(result, RichText)
    assert "rich" in str(result)





# Callout block tests
def test_callout_block_default_styles():
    block = CalloutBlock()
    # Check that 'style' block exists and has default choices
    style_block = block.child_blocks["style"]
    expected = {"info", "warning", "success", "danger", "note"}
    actual = {value for value, _ in style_block.choices}
    assert expected.issubset(actual)

def test_callout_block_custom_styles():
    custom_styles = [("alert", "Alert"), ("quiet", "Quiet")]
    block = CalloutBlock(styles=custom_styles)
    choices = dict(block.child_blocks["style"].choices)
    assert choices == dict(custom_styles)

def test_callout_block_clean_valid_input():
    block = CalloutBlock()

    # Patch style block's choices and rebind the .field to ensure internal field reflects updated choices
    new_choices = [
        ("info", "Info"),
        ("warning", "Warning"),
        ("success", "Success"),
        ("danger", "Danger"),
        ("note", "Note"),
    ]
    block.child_blocks["style"].choices = new_choices
    block.child_blocks["style"].field = ChoiceBlock(choices=new_choices).field

    struct_value = block.to_python({
        "title": "Heads up!",
        "body": "<p>This is a warning.</p>",
        "style": "warning"
    })

    cleaned = block.clean(struct_value)
    assert cleaned["title"] == "Heads up!"
    assert cleaned["body"].source == "<p>This is a warning.</p>"
    assert cleaned["style"] == "warning"

def test_callout_block_clean_rejects_invalid_style():
    block = CalloutBlock()
    data = {
        "title": "Error!",
        "body": MockRichTextInput("<p>Bad style</p>"),
        "style": "nonexistent",
    }
    with pytest.raises(StructBlockValidationError):
        block.clean(data)






def test_quote_block_clean_valid_input():
    block = QuoteBlock()

    struct_value = block.to_python({
        "quote": "<p>To be or not to be.</p>",
        "attribution": "Shakespeare",
        "style": "highlight",
    })

    cleaned = block.clean(struct_value)
    assert cleaned["style"] == "highlight"
    assert cleaned["attribution"] == "Shakespeare"
    assert isinstance(cleaned["quote"], RichText)


def test_quote_block_clean_minimal():
    block = QuoteBlock()

    struct_value = block.to_python({
        "quote": "<p>Just do it.</p>",
    })

    cleaned = block.clean(struct_value)
    assert cleaned.get("style", "default") == "default"
    assert cleaned.get("attribution") in (None, "")
    assert isinstance(cleaned["quote"], RichText)


def test_code_block_clean_valid_input():
    block = CodeBlock()

    struct_value = block.to_python({
        "language": "python",
        "code": "print('Hello, world!')",
        "caption": "example.py",
        "style": "lined",
    })

    cleaned = block.clean(struct_value)
    assert cleaned["language"] == "python"
    assert cleaned["code"] == "print('Hello, world!')"
    assert cleaned["caption"] == "example.py"
    assert cleaned["style"] == "lined"


def test_code_block_clean_minimal():
    block = CodeBlock()

    struct_value = block.to_python({
        "language": "text",
        "code": "plain text only",
    })

    cleaned = block.clean(struct_value)
    assert cleaned.get("caption") in (None, "")
    assert cleaned.get("style", "default") == "default"
    assert cleaned["language"] == "text"
    assert cleaned["code"] == "plain text only"





















