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
python manage.py runserver



