ARG image_tag=latest
FROM libero/content-store_venv:${image_tag} as venv
FROM python:3.6.6-alpine3.8

WORKDIR /app
COPY api/ api/
COPY --from=venv /.venv/ /.venv/
ENV PYTHONUSERBASE=/.venv PATH=/.venv/bin:$PATH

CMD ["python"]
