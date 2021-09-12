from django.contrib import admin

# Register your models here.
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'writer',
        'image',
        'success',
        'updated_at'
    )
    list_display_links = (
        'title',
        'writer'
    )


admin.site.register(models.Challenge, PostAdmin)