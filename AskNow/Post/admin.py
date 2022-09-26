from django.contrib import admin
from Post.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug',
                    'date_published', 'date_updated']

admin.site.register(Comment)
