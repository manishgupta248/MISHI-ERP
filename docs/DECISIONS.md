# MISHI-ERP — Architectural Decisions

# Phase -1

## Decision 001 — Django Project Name
The Django project is named `Mishika`.

## Decision 002 — Core Application
A dedicated `core` Django application will provide common foundation functionality.

## Decision 003 — Shared Templates and Static
Project-level `templates/` and `static/` directories are used for shared resources.

Individual applications may later contain app-specific templates and static files when justified.

## Decision 004 — Initial Database
SQLite is used during the foundation and early development stages.

A future PostgreSQL migration will be considered when the system requirements justify it.

## Decision 005 — Environment Configuration
Environment-specific and secret configuration is stored in `.env` and excluded from Git.

## Decision 006 — Python Environment
The project uses an isolated `.venv` virtual environment.

## Decision 007 — Custom User Model
A custom `accounts.User` model (extending AbstractUser) is used instead of
Django's default, to allow future ERP-specific fields and role/permission
logic without a disruptive migration.

## Decision 008 — App-Namespaced URLs
Each Django app owns its own urls.py with an app_name namespace
(e.g. "core:home") to avoid name collisions as more apps are added.

## Decision 009 — Shared TimeStampedModel
An abstract base class `core.models.TimeStampedModel` provides
created_at/updated_at fields. All future app models should inherit
from it instead of redefining these fields individually.

## Decision 010 — To-Do App as First ERP Module
A new `todo` app was introduced as the first real ERP feature module,
following the app-namespaced URL convention established in Phase 1.
Tasks are owned per-user (ForeignKey to accounts.User).

## Decision 011 — REST API Introduced Early
Django REST Framework (already a dependency but previously unused) is
now active, starting with /api/tasks/. This is intentionally built
ahead of need, because the planned Telegram bot (Phase 5) and any
future integrations will require a non-browser entry point to ERP
data. All API endpoints are scoped to the authenticated user's own
records.

## Decision 012 — Recurrence Stored as Label Only
Task.repeat_label records the user's intended recurrence (Daily/
Weekly/Monthly) but does not yet trigger any automatic behavior.
Actual recurring-task automation is deferred to the future Events/
Automation phase, to avoid building scheduling logic prematurely.