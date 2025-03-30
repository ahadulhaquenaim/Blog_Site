from django.contrib import admin
from .models import Post, Author, Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('tags', 'author', 'date')
    list_display = ('title', 'author', 'date')
    prepopulated_fields = {'slug': ('title',)}  # Automatically fill the slug field based on the title


admin.site.register(Post, PostAdmin)  # Register the Post model with the custom admin class
admin.site.register(Author)
admin.site.register(Tag)
