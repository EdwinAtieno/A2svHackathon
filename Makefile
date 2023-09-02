install:
	python3 -m pip install -r requirements.pip

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

serve:
	python3 manage.py runserver 8001
