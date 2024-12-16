FROM python:3.12.7-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

RUN pip install pipx && \
    pipx install poetry==1.8.4

ENV PATH="/root/.local/bin:${PATH}"

RUN poetry config virtualenvs.create true

COPY .env .

COPY ./pyproject.toml . 

COPY ./main.py . 

COPY ./src /app/src  

RUN poetry install --no-interaction --no-ansi


WORKDIR /app

CMD ["poetry", "run", "python", "main.py"]