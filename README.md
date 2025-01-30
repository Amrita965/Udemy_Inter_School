## Installation

```bash
git clone https://github.com/your-username/school-management-system.git
cd school-management-system
pip install pipenv
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
