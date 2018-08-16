Libero content store
====================

## Development

Building images:
```
docker-compose build
```

Running the application:
```
docker-compose up -d
```

Running the application locally (to be removed when Docker becomes the primary development mode):
```
FLASK_APP=api/api.py pipenv run flask run
```

Checking the application is responding:
```
curl -v localhost:5000/ping
```

Running tests:
```
docker-compose run cli python -m pytest
```
