init:
	pip install --upgrade pip
	pip install -r requirements.txt

run:
	python './src/file_organizer/project.py'

up:
	pip freeze > requirements.txt

format:
	black './src/file_organizer'
	black './tests'

test:
	python -m pytest .

check:
	ruff check

fix:
	ruff check --fix
