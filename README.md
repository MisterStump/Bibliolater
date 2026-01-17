# Bibliolater

A project created with FastAPI CLI.

## Quick Start

### Start the development server

```bash
uv run fastapi dev
```

Visit http://localhost:8000

### Deploy to FastAPI Cloud

> FastAPI Cloud is currently in private beta. Join the waitlist at https://fastapicloud.com

```bash
uv run fastapi login
uv run fastapi deploy
```

## Project Structure

- `main.py` - Your FastAPI application
- `pyproject.toml` - Project dependencies

## Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [FastAPI Cloud](https://fastapicloud.com)

# How to deploy containers and test
* Outside of the dev environment, run server with `docker compose up --build`
* When it is running hit W to watch for changes
    * This is dependent on the `develop` section of the docker-compose
* Now changes will be monitored and any saved change will be synced into the container



In my current project, when I use the alembic command line `uv run alembic revision -m "message"`, followed by `uv run alembic upgrade head`, the version is not stored in the migrations/versions folder. Instead it is being saved locally in the docker in a migrations/revisions folder. How do I fix this so I can commit my revision list to github?