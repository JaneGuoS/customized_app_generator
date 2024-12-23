from django.contrib import admin

from .models import Channel, Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class ChannelAdmin(admin.ModelAdmin):
    search_fields = ('title', 'count', "created_date")
    list_filter = ['status', 'title']
    date_hierarchy = "created_date"

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]
    search_fields = ('title', 'body', "published_date")
    list_filter = ['published', 'title']
    date_hierarchy = "published_date"

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)