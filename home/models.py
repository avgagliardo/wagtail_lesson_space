from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager


class LessonPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'LessonPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class LessonPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    domain = models.CharField(max_length=100)

    tags = ClusterTaggableManager(through=LessonPageTag, blank=True)

    body = StreamField([
        ("heading", blocks.CharBlock()),
        ("paragraph", blocks.RichTextBlock()),
        ("image", ImageChooserBlock()),
        ("latex", blocks.TextBlock(help_text="Wrap your LaTeX in $$...$$ or \\(...\\)")),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("domain"),
        FieldPanel("tags"),
        FieldPanel("body"), 
    ]

class HomePage(Page):
    template = "home/home_page.html"        








