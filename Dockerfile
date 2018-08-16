ARG image_tag=latest
ARG python_base_image_tag
FROM libero/content-store_venv:${image_tag} as venv
FROM python:${python_base_image_tag}

WORKDIR /app
COPY api/ api/
COPY --from=venv /.venv/ /.venv/
ENV PYTHONUSERBASE=/.venv PATH=/.venv/bin:$PATH

CMD ["python"]
