from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase


admin.site.register(Image)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['place', 'image', 'preview_image']
    readonly_fields = ["preview_image"]
    ordering = ['my_order']

    def preview_image(self, place):
        return format_html(
            '<img src="{}" width="auto" height="200px"/>',
            place.image.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
