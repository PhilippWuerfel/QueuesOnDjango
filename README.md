# QueuesOnDjango
Setup with Celery + Django including message broker and result backend
Credits to https://testdriven.io/courses/django-celery/ for giving such nice tutorials and explanations.

## Local Setup

Start processes locally, workdir is at level of manage.py
- `celery -A dj_queues worker --loglevel=info` - Spin up celery worker in terminal
- `celery -A dj_queues flower --port=5555` - Spin up flower monitoring

## Docker
- `docker-compose exec <service-name> bash` - Execute bash on docker service

## Testing, Linting, Formating
We use Pytest for unit tests, flake8 for codestyle checks, black & isort for code formatting.
- `python -m pytest` - Run pytest<br>
- `python -m flake8 .` - Code style check via flake8 <br>
- `python -m black --check --exclude=migrations .` - Check black code format <br>
- `python -m black --check --exclude='migrations|packages' .` - Check black code format excluding multiple directories <br>
- `python -m black --diff --exclude='migrations|packages' .` - Show diffs in black code format <br>
- `python -m black --exclude='migrations|venv' .` - Run black code formatter
- `python -m isort . --check-only --skip='migrations' --skip='venv' --profile='black'` - Check isort code format
- `python -m isort . --diff--skip='migrations' --skip='venv' --profile='black'` - Show diffs isort code format
- `python -m isort . --skip='migrations' --skip='venv' --profile='black'` - Execute isort code format
