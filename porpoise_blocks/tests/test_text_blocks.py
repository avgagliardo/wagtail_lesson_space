import pytest
from wagtail.rich_text import RichText
from porpoise_blocks.text_blocks import HeadingBlock, ParagraphBlock

def test_heading_block_meta():
    block = HeadingBlock()
    assert block.meta.label == "Heading"
    assert block.meta.icon == "title"
    # help_text is not directly accessible — skip it



def test_heading_block_clean():
    block = HeadingBlock()
    result = block.clean("Introduction")
    assert result == "Introduction"


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
