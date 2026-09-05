from django.db import models

# Model for Database Back-up Service

class BackupRecord(models.Model):
    """Stores information about each database backup."""

    filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    file_size = models.PositiveBigIntegerField(default=0)
    status = models.CharField(max_length=20, default="SUCCESS")
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.filename

# ================================================

class TimeStampedModel(models.Model):
    """
    Abstract base class adding created/updated timestamps.
    Any model in any app can inherit this instead of redefining
    created_at/updated_at every time.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # this itself never becomes a database table

# =====================================================