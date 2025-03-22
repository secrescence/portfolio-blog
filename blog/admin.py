from django.contrib import admin
from .models import BlogPost

# Register your models here.
admin.site.register(BlogPost)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    search_fields = ("title", "content")
    list_filter = ("category", "created_at")
