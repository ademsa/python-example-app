FROM python:3

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

EXPOSE 3000

CMD ["python", "./main.py"]