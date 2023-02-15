from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('title', 'description', 'creation_date', 'status', 'author', )
    search_fields = ('title', 'autor', 'description')
    readonly_fields = ('creation_date', 'edited_time')
    ordering = ('-creation_date', '-edited_time',)
    list_filter = ['status', 'creation_date', 'author']

