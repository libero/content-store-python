# Libero content store

## Development

Building images:

```bash
docker-compose build
```

Running the application:

```bash
docker-compose up -d
```

Running the application locally (to be removed when Docker becomes the primary development mode):
For non-development configuration set APP_SETTINGS environment variable to the module to use.
Defaults to `content_store.api.config.DevelopmentConfig`

```bash
FLASK_APP=content_store/api/api.py PYTHONPATH=. pipenv run flask run
```

Checking the application is responding:

```bash
curl -v localhost:5000/ping
```

Running tests:

```bash
docker-compose run web python -m pytest
```
