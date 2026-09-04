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