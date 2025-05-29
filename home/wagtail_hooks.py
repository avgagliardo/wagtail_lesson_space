from wagtail_modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import LessonPage


class LessonPageAdmin(ModelAdmin):
    model = LessonPage
    menu_label = "Lessons"
    menu_icon = "doc-full"  # You can pick from https://docs.wagtail.org/en/stable/topics/icons.html
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "subtitle", "domain")
    search_fields = ("title", "subtitle", "domain", "tags__name")


modeladmin_register(LessonPageAdmin)
