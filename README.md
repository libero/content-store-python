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

Checking the application is responding:
```
curl -v localhost:5000/ping
```

Running tests:
```
docker-compose run cli python -m pytest
```
