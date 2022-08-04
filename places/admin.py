from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["preview_image"]

    def preview_image(self, place):
        return format_html(
            '<img src="{}" width="auto" height="200px"/>',
            place.image.url
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
