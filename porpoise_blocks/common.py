from porpoise_blocks.text_blocks import HeadingBlock, ParagraphBlock
from porpoise_blocks.text_blocks import CalloutBlock, QuoteBlock, CodeBlock
from porpoise_blocks.math_blocks import LaTeXBlock

ESSENTIAL_BLOCKS = [
    ("heading", HeadingBlock()),
    ("paragraph", ParagraphBlock()),
    ("callout", CalloutBlock()),
    ("quote", QuoteBlock()),
    ("code", CodeBlock()), 
    ("latex", LaTeXBlock()),    
]