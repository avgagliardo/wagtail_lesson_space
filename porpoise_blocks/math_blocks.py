from wagtail.blocks import TextBlock

class LaTeXBlock(TextBlock):
    class Meta:
        icon = "code"
        label = "LaTeX"
        template = "porpoise_blocks/latex_block.html"