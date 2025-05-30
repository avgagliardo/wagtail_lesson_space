from porpoise_blocks.text_blocks import HeadingBlock, ParagraphBlock
from porpoise_blocks.text_blocks import CalloutBlock, QuoteBlock, CodeBlock

ESSENTIAL_BLOCKS = [
    ("heading", HeadingBlock()),
    ("paragraph", ParagraphBlock()),
    ("callout", CalloutBlock()),
    ("quote", QuoteBlock()),
    ("code", CodeBlock()),  
]