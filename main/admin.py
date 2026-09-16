from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "featured",
    )