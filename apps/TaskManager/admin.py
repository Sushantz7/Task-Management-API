from django.contrib import admin
from .models import Project, Task, Comment


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at", "updated_at")


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)
