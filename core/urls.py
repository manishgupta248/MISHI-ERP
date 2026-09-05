"""
URL routes belonging to the core app.
Using app_name="core" means these routes are referenced elsewhere as
'core:home', 'core:create_backup', 'core:backup_list' — this avoids name
clashes once more apps are added later (Finance, Tasks, Events, etc.).
"""

from django.urls import path

from core.views import backup_list, create_backup, home

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("backup/create/", create_backup, name="create_backup"),
    path("backups/", backup_list, name="backup_list"),
]