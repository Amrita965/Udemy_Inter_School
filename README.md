## Installation

```bash
# 1. Clone the repository and navigate to the project folder
git clone https://github.com/your-username/school-management-system.git
cd school-management-system

# 2. Install dependencies and set up the virtual environment
pip install pipenv
pipenv install
pipenv shell

# 3. Set up the database
python manage.py migrate

# 4. Create a superuser (optional, for admin access)
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
