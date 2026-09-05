import logging
import shutil
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.db import connection

from core.constants.system import (
    BACKUP_STATUS_FAILED,
    BACKUP_STATUS_SUCCESS,
)
from core.exceptions.base import MishiERPError
from core.models import BackupRecord


logger = logging.getLogger("mishi.backup")


def create_database_backup():
    """
    Create a timestamped SQLite database backup
    and record the result.
    """

    database_path = Path(settings.DATABASES["default"]["NAME"])
    backup_directory = settings.BASE_DIR / "backup"

    if connection.vendor != "sqlite":
        raise MishiERPError(
            "The current backup service supports SQLite only."
        )

    if not database_path.exists():
        raise MishiERPError("Database file was not found.")

    backup_filename = None

    try:
        backup_directory.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"db_backup_{timestamp}.sqlite3"
        backup_path = backup_directory / backup_filename

        # Ensure Django has closed any pending database work.
        connection.close()

        shutil.copy2(database_path, backup_path)

        file_size = backup_path.stat().st_size

        backup = BackupRecord.objects.create(
            filename=backup_filename,
            file_size=file_size,
            status=BACKUP_STATUS_SUCCESS,
        )

        logger.info(
            "Database backup created successfully: %s",
            backup_filename,
        )

        return backup

    except OSError as exc:
        logger.error(
            "Database backup failed: %s",
            exc,
        )

        if backup_filename:
            BackupRecord.objects.create(
                filename=backup_filename,
                status=BACKUP_STATUS_FAILED,
                notes=str(exc),
            )

        raise MishiERPError(
            f"Unable to create database backup: {exc}"
        ) from exc