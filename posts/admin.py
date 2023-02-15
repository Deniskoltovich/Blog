from django.contrib import admin
from .models import Post



@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('blog', 'title', 'content', 'created_time', 'edited_time', 'status', )
    search_fields = ('title', 'blog__title',)
    readonly_fields = ('created_time', 'edited_time')
    ordering = ('-created_time', 'edited_time',)
    list_filter = ['status', 'created_time', 'blog']

