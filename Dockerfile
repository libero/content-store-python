ARG image_tag=latest
ARG python_base_image_tag
FROM libero/content-store_venv:${image_tag} as venv
FROM python:${python_base_image_tag}

COPY --from=venv /.venv/ /.venv/
ENV PYTHONUSERBASE=/.venv PATH=/.venv/bin:$PATH

WORKDIR /app
COPY api/ api/
# if there is work to be done here, move the venv copying after it

CMD ["python"]
