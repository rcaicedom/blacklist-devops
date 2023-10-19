FROM python:3.11.4-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="$PYTHONPATH:/usr/blacklist"
ENV POETRY_HOME="/usr/local"
ENV TEST_COVERAGE=false
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -
WORKDIR /usr/blacklist
COPY . .
RUN poetry install --no-root
EXPOSE 5000
ENTRYPOINT ["bash", "./entrypoint.sh" ]