from django.contrib import admin

# Register your models here.
from core.models import BackupRecord


@admin.register(BackupRecord)
class BackupRecordAdmin(admin.ModelAdmin):
    list_display = ("filename", "created_at", "file_size", "status", )

    list_filter = ("status", "created_at")

    search_fields = ("filename", "notes")

    readonly_fields = ("filename", "created_at","file_size", "status",)

