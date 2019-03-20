from django.contrib import admin

#Models
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment Admin"""
    list_display = ('id', 'user', 'post', 'description', 'created')
