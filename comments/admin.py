from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('news_id', 'date', 'content', 'author')
    readonly_fields = ('date',)

