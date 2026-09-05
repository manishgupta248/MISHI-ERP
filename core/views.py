from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.exceptions.base import MishiERPError
from core.models import BackupRecord
from core.services.backup import create_database_backup


@login_required
def home(request):
    """Display the MISHI-ERP dashboard, including a live summary from other apps."""
    from todo.models import Task  # local import: dashboard aggregates data from other apps

    pending_tasks_count = Task.objects.filter(
        owner=request.user, status=Task.Status.PENDING,
    ).count()

    return render(request, "dashboard.html", {"pending_tasks_count": pending_tasks_count})


@login_required
def create_backup(request):
    """Create a database backup from the dashboard."""
    if request.method == "POST":
        try:
            backup = create_database_backup()
            messages.success(request, f"Backup created successfully: {backup.filename}")
        except MishiERPError as exc:
            messages.error(request, f"Backup failed: {exc}")
    return redirect("core:home")


@login_required
def backup_list(request):
    """Display the database backup history."""
    backups = BackupRecord.objects.all()
    return render(request, "backups/list.html", {"backups": backups})