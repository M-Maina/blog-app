from django.contrib import admin
from .models import Author, Tag, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author", "date")
    list_filter = ("title","author", "tags", "date")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

