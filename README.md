## Installation

# 1. Clone the repository and navigate to the project folder

```bash
git clone https://github.com/your-username/school-management-system.git
cd school-management-system
```

# 2. Install dependencies and set up the virtual environment
```bash
pip install pipenv
```
pipenv install
```
pipenv shell
```

# 3. Set up the database
```
python manage.py migrate
```
# 4. Create a superuser (optional, for admin access)
```
python manage.py createsuperuser
```

# 5. Run the development server
```
python manage.py runserver
```

## Usage

- Navigate to the Django admin panel at `http://127.0.0.1:8000/admin/` to manage students, teachers, courses, and attendance.
- You can log in using the following credentials (default for admin access):
  - **Username**: admin
  - **Password**: admin
- Students and teachers can log in to their respective dashboards and access their data.
