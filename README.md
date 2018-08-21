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
For non-development configuration set APP_SETTINGS environment variable to the module to use. Defaults to `content_store.api.config.DevelopmentConfig`

```
FLASK_APP=content_store/api/api.py PYTHONPATH=. pipenv run flask run
```

Checking the application is responding:
```
curl -v localhost:5000/ping
```

Running tests:
```
docker-compose run app python -m pytest
```

Installing a new package:
```
docker-compose build
docker-compose run --rm venv /bin/sh -c 'pipenv install requests && pipenv lock'
```
