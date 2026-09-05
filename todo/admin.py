from django.contrib import admin

from todo.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "classification", "status", "priority", "due_at")
    list_filter = ("status", "classification", "priority")
    search_fields = ("title", "description")
    date_hierarchy = "due_at"