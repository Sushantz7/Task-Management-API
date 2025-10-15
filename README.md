# Task-Management-API
Building a Task Management API using Django Rest Framework.

This README shows the basic steps to get the project running locally: install Python, create a virtual environment, install dependencies, run migrations, and start the dev server.

---

## Prerequisites
- Git
- Python **3.10+**
- `pip` (comes with Python)

---

## Quick Start

### 1. Clone the repo
```bash
https://github.com/Sushantz7/Task-Management-API.git
cd Task-Management-API.
```

### 2. Create and activate Virtual Environment
macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows(PowerShell)
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows(cmd.exe)
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Create a superuser
To access the Django admin page.
```bash
python manage.py createsuperuser
```

### 6. .env File sample 
```bash
DJANGO_SECRET_KEY=your-secret-key-here

# Debug mode (use True for development, False in production)
DEBUG=True

# Allowed hosts (comma-separated, e.g. 127.0.0.1,localhost,mydomain.com)
ALLOWED_HOSTS=127.0.0.1,localhost

# Database configuration (SQLite default)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Example PostgreSQL config (uncomment and fill if needed)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

```
### 7. Run the Development Server
```bash
python manage.py runserver
```
Now by clicking on the provided link on the terminal you can access the API View.
