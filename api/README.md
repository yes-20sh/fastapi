# FastAPI Modular Backend

Feature-based FastAPI starter with centralized SQLAlchemy models, OOP services,
and no repository layer. Dependencies are managed with **uv**.

## Requirements

- Python 3.11+
- uv

Install uv if needed:
```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

```bash
# Create and activate the project environment and install dependencies
uv sync

# Copy environment template (Windows PowerShell)
Copy-Item .env.example .env

# macOS / Linux
cp .env.example .env
```

## Run

```bash
uv run api
```

Or run Uvicorn directly:
```bash
uv run uvicorn app.main:app --reload
```

Open Swagger docs at http://127.0.0.1:8000/docs.

## Tests and lint

```bash
uv run pytest
uv run ruff check .
```

## Dependency management

```bash
uv add package-name
uv add --dev package-name
uv remove package-name
uv sync
uv lock
uv tree
```

`uv sync` creates/updates `uv.lock` when needed. Commit both `pyproject.toml`
and `uv.lock` to version control after the first successful sync.

## Main endpoints

- `GET /health` (Ping)
- `GET /api/v1/health` (Get all health records from database)
- `POST /api/v1/health` (Create health record with name and date/time)

SQLite is used by default. Configure `DATABASE_URL` in `.env` to use another
SQLAlchemy-supported database. For PostgreSQL, install a driver such as
`psycopg[binary]` with `uv add "psycopg[binary]"`.

For production, configure a strong secret key, use HTTPS, add authorization
roles, use Alembic migrations instead of `Base.metadata.create_all()`, and
add integration tests.
