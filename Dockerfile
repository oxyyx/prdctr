FROM python:3.10.1

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV POETRY_PYTHONPATH "${POETRY_PYTHONPATH}:/app"

EXPOSE 8000
WORKDIR /app


COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.1
RUN poetry install --no-dev

COPY . ./

CMD ["scripts/run-app.sh"]