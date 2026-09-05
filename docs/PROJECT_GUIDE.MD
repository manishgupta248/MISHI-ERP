mkdir D:\Mishi-ERP
cd D:\Mishi-ERP

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"

python -m pip install --upgrade pip
python -m pip install Django djangorestframework python-dotenv Pillow requests

python -m pip freeze > requirements.txt

django-admin startproject Mishika .
python manage.py startapp core

New-Item -ItemType Directory -Force templates
New-Item -ItemType Directory -Force static
New-Item -ItemType Directory -Force data
New-Item -ItemType Directory -Force backup
New-Item -ItemType Directory -Force docs

ni .env
python manage.py check
python manage.py migrate
python -m django --version

ni .gitignore
git init
git branch -M main
git remote add origin https://github.com/manishgupta248/MISHI-ERP.git
git remote -v
git status
#==========================================

New-Item -ItemType File -Force docs\CURRENT_STATE.md
New-Item -ItemType File -Force docs\TODO.md
New-Item -ItemType File -Force docs\DECISIONS.md
New-Item -ItemType File -Force docs\ARCHITECTURE.md
New-Item -ItemType File -Force docs\HANDOFF.md
New-Item -ItemType File -Force docs\ROADMAP.md
New-Item -ItemType File -Force backup\.gitkeep

#===========================================================
python manage.py createsuperuser
python manage.py runserver

#=====================================================
git add .
git commit -m "Phase 1: establish Django foundation"
git reset docs/PROJECT_GUIDE.MD
git push -u origin main

# =====================================================
# Delete the old database file
Remove-Item -Force .\data\db.sqlite3 -ErrorAction SilentlyContinue

# Delete old backup files (keeps the backup folder itself via .gitkeep)
Get-ChildItem -Path .\backup -Filter "db_backup_*.sqlite3" | Remove-Item -Force

# Delete old core migrations (keep __init__.py so it's still a valid Python package)
Get-ChildItem -Path .\core\migrations -Exclude "__init__.py" | Remove-Item -Force

# Generate a strong secret key to put in your .env file
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# ======================================================
# to Install self-hosted frontend assets - Bootstrap + Alpine

New-Item -ItemType Directory -Force static\vendor\bootstrap\css
New-Item -ItemType Directory -Force static\vendor\bootstrap\js
New-Item -ItemType Directory -Force static\vendor\alpine

Invoke-WebRequest "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" -OutFile "static\vendor\bootstrap\css\bootstrap.min.css"

Invoke-WebRequest "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" -OutFile "static\vendor\bootstrap\js\bootstrap.bundle.min.js"

Invoke-WebRequest "https://cdn.jsdelivr.net/npm/alpinejs@3.14.3/dist/cdn.min.js" -OutFile "static\vendor\alpine\alpine.min.js"

# =======================================================
New-Item -ItemType Directory -Force templates\partials
New-Item -ItemType Directory -Force static\css
New-Item -ItemType Directory -Force static\js

New-Item -ItemType File -Force templates\base.html
New-Item -ItemType File -Force templates\dashboard.html
New-Item -ItemType File -Force templates\partials\_navbar.html
New-Item -ItemType File -Force templates\partials\_sidebar.html
New-Item -ItemType File -Force templates\partials\_footer.html
New-Item -ItemType File -Force static\css\app.css

# ====
# MISHI-ERP — Project Development Guide

## 1. Project Purpose

MISHI-ERP is a modular Personal ERP and AI Agentic System.

The system will combine:

* Django-based ERP applications
* Common core services
* Events and scheduling
* Telegram integration
* AI and LLM services
* Agentic workflows
* Permissions and controlled actions
* Document and data management

The project is intended to grow incrementally while maintaining a stable and understandable architecture.

## 2. Development Environment

Operating System:
Windows

Project Root:

D:\Mishi-ERP

Primary Tools:

* Python 3.13.3
* Django
* Django REST Framework
* VS Code
* Git
* PowerShell

Python environment:

.venv

## 3. Development Principles

1. Develop incrementally.
2. Do not add unnecessary dependencies.
3. Keep Django applications modular.
4. Keep shared functionality inside `core` only when it is genuinely shared.
5. Keep secrets and environment-specific configuration outside source code.
6. Prefer simple and deterministic solutions.
7. Test each meaningful development step.
8. Document important architectural decisions.
9. Avoid premature AI/LLM complexity.
10. Preserve backward compatibility when practical.

## 4. Project Structure

MISHI-ERP/
│
├── .venv/
├── Mishika/
├── core/
├── templates/
├── static/
├── data/
├── backup/
├── docs/
├── manage.py
├── requirements.txt
├── .env
└── .gitignore

Future Django applications will be added as independent modules.

## 5. Django Architecture

`Mishika` is the Django project containing global configuration.

`core` is the foundational Django application.

The `core` application should contain only functionality that is genuinely common across multiple applications.

Business-specific functionality should normally belong to its own Django application.

## 6. Templates and Static Files

Shared templates are maintained under:

templates/

Shared static resources are maintained under:

static/

Large applications may later contain their own application-specific templates and static directories.

## 7. Configuration

Environment-specific values must be stored in `.env`.

Examples include:

* Secret keys
* API credentials
* Bot tokens
* Database credentials
* External service configuration

`.env` must never be committed to Git.

## 8. Database Strategy

SQLite is being used during the foundation and early development stages.

PostgreSQL may be introduced when the system requirements justify it.

Database architecture should be designed so that migration to PostgreSQL remains practical.

## 9. Dependency Management

Python packages are installed inside `.venv`.

After meaningful dependency changes:

```
python -m pip freeze > requirements.txt
```

Only necessary packages should be added.

## 10. Git Workflow

The `main` branch represents the stable project baseline.

Development should normally follow:

1. Make a small, focused change.
2. Test the change.
3. Review the Git diff.
4. Commit with a meaningful message.
5. Push when the change is stable.

Example:

```
git status
git diff
python manage.py check
git add .
git commit -m "Clear description of change"
git push
```

## 11. Documentation

The following documents are maintained under `docs/`:

* CURRENT_STATE.md — current development condition
* TODO.md — pending work
* DECISIONS.md — important architectural decisions
* ARCHITECTURE.md — system architecture
* HANDOFF.md — information required to continue development
* ROADMAP.md — planned development phases
* PROJECT_GUIDE.MD — overall development rules

Documentation should be updated when the project state or architecture materially changes.

## 12. Development Method

Development will proceed phase by phase.

Each meaningful step should have:

* Clear objective
* Exact commands
* Required file changes
* Minimal but useful comments
* Smoke test
* Git checkpoint where appropriate
* Documentation update when required

No major architectural change should be introduced without first recording the reason for the change.

## 13. AI and Agentic Development Rule

AI/LLM functionality will be introduced as a controlled layer.

ERP business logic must not depend directly on an LLM.

The AI layer should interact with the ERP through defined services, tools, permissions and controlled interfaces.

The system should remain functional even if an LLM service is unavailable.

## 14. Security Principles

Never commit:

* `.env`
* API keys
* passwords
* authentication tokens
* private certificates
* personal credentials

Production security requirements will be addressed separately before deployment.

## 15. Current Development State

Phase 1 — Foundation

Completed:

* Python environment
* Virtual environment
* Django project
* Core application
* Initial dependencies
* Shared templates/static directories
* SQLite database
* Environment configuration
* Git repository
* GitHub remote
* Initial documentation
* Foundation landing page
* Initial Git commit and push

## 16. Next Objective

Continue Phase 1 foundation work with:

* Review and refine project structure
* Establish reusable core conventions
* Complete foundation smoke tests
* Establish development documentation workflow
* Prepare the project for subsequent Django applications

