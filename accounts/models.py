from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model for MISHI-ERP.

    It currently behaves exactly like Django's default User.
    The point of doing this now is future-proofing: once permissions,
    roles, or ERP-specific profile fields are needed (Phase 2+), we can
    add them here without a disruptive migration later.
    """
    pass