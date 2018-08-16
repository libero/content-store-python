ARG image_tag=latest
FROM libero/content-store_venv:${image_tag} as venv
FROM python:3.6.6-alpine3.8

WORKDIR /app
COPY api/ api/
COPY --from=venv /app/.venv/ .venv/

CMD [".venv/bin/python"]
