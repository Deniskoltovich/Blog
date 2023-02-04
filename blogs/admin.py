from django.contrib import admin
from .models import Blog, ModelChangeLogsModel


admin.site.register(Blog)
admin.site.register(ModelChangeLogsModel)
