Libero content store
====================

## Development

Running the app:
```
FLASK_APP=api/api.py pipenv run flask run
```

## Docker setup

Build images:
```
docker-compose build
```

Run the application:
```
docker-compose up -d
```

Run tests:
```
docker-compose run cli .venv/bin/python -m pytest
```
