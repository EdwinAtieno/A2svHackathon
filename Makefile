install:
	python3 -m pip install -r requirements.txt

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

serve:
	python3 manage.py runserver

super:
	python3 manage.py createsuperuser
