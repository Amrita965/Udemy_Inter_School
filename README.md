Installation

Prerequisites

Python (>=3.8 recommended)

Pipenv (for managing virtual environments)

PostgreSQL/MySQL (optional, default is SQLite)

Setup

Clone the repository:

git clone https://github.com/yourusername/school-management.git
cd school-management

Create and activate a virtual environment using Pipenv:

pipenv shell

Install dependencies:

pipenv install

Configure the database in settings.py (default is SQLite, update if using PostgreSQL/MySQL).

Run database migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Start the development server:
