from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class Task(TimeStampedModel):
    """A single to-do item, official or personal, owned by one user."""

    class Classification(models.TextChoices):
        OFFICIAL = "OFFICIAL", "Official"
        PERSONAL = "PERSONAL", "Personal"
        OTHER = "OTHER", "Other"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    class Priority(models.IntegerChoices):
        # Numbers (not text) so "sort by priority" actually orders High > Medium > Low
        LOW = 1, "Low"
        MEDIUM = 2, "Medium"
        HIGH = 3, "High"

    class Repeat(models.TextChoices):
        NONE = "NONE", "Does not repeat"
        DAILY = "DAILY", "Daily"
        WEEKLY = "WEEKLY", "Weekly"
        MONTHLY = "MONTHLY", "Monthly"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    classification = models.CharField(
        max_length=20, choices=Classification.choices, default=Classification.PERSONAL,
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING,
    )
    priority = models.IntegerField(
        choices=Priority.choices, default=Priority.MEDIUM,
    )

    due_at = models.DateTimeField(null=True, blank=True)

    related_link = models.URLField(blank=True)
    attachment = models.FileField(
        upload_to="task_attachments/%Y/%m/", blank=True, null=True,
    )

    # Informational only for now — no automatic recreation of repeated
    # tasks yet. Real recurrence logic belongs in the future Events/
    # Automation phase.
    repeat_label = models.CharField(
        max_length=10, choices=Repeat.choices, default=Repeat.NONE,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

# ============================================================