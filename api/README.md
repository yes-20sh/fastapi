# FastAPI Modular Backend

> A modern, modular FastAPI backend powered by PostgreSQL and SQLAlchemy, featuring clean service-layer architecture, custom route decorators, robust connection verification, and dependency management using uv.

---

## Features

- **Modular Architecture**: Feature-based organization (`modules/`, `models/`, `core/`, `shared/`).
- **Clean Layered Design**:
  - **Controllers**: Strictly manage HTTP requests and responses without database leakage.
  - **Services**: Encapsulate all database queries, transactions, rollbacks, and business logic.
- **Custom Route Decorators**: Simplified `@GET()` and `@POST()` decorators that auto-infer route paths from function names and tags from module folders.
- **PostgreSQL / Supabase Ready**: SQLAlchemy 2.0 with modern `psycopg` binary driver and connection pooling.
- **Robust Startup Verification**: Automatically checks database connectivity on startup; safely aborts server initialization if unreachable.
- **Fast Package Management**: Managed with [**uv**](https://docs.astral.sh/uv/) for ultra-fast dependency resolution and virtual environments.

---

## Project Structure

```text
fastapi-learn/
└── api/
    ├── app/
    │   ├── core/
    │   │   ├── config/          # Database connection, engine, and connection checks
    │   │   └── middleware/      # CORS and global exception handlers
    │   ├── models/              # Centralized SQLAlchemy ORM models
    │   ├── modules/
    │   │   └── health/          # Feature module: controller, service, schema
    │   ├── shared/
    │   │   └── decorator/       # Custom @GET, @POST routing decorators
    │   └── main.py              # Application entrypoint & lifespan management
    ├── tests/                   # Automated unit & integration tests
    ├── .env.example             # Environment variable template
    ├── pyproject.toml           # Project dependencies and configurations
    └── README.md
```

---

## Getting Started

### Prerequisites

- **Python 3.11+**
- [**uv**](https://docs.astral.sh/uv/) installed:
  ```bash
  # Windows (PowerShell)
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

  # macOS / Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Installation

1. Navigate to the `api` directory:
   ```bash
   cd api
   ```

2. Install dependencies and set up the virtual environment:
   ```bash
   uv sync
   ```

3. Configure your environment variables:
   ```bash
   # Copy template
   cp .env.example .env     # macOS / Linux
   Copy-Item .env.example .env   # Windows PowerShell
   ```

4. Update your `.env` with your PostgreSQL / Supabase connection string:
   ```env
   DATABASE_URL=postgresql://user:password@host:5432/postgres
   CORS_ORIGINS=http://localhost:3000,http://localhost:5173
   ```

---

## Running the Application

From inside the `api` directory:

```bash
uv run api
```

Or run directly with Uvicorn:
```bash
uv run uvicorn app.main:app --reload
```

- **Interactive API Docs (Swagger)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative Docs (ReDoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Service health ping (`status: ok`) |
| `GET` | `/health` | Alternate health ping |
| `GET` | `/api/v1/get_all_health` | Retrieve all health records from database |
| `POST` | `/api/v1/create_health` | Create a new health record |

---

## Testing and Linting

Run automated unit tests:
```bash
uv run pytest
```

Check code style and linting with Ruff:
```bash
uv run ruff check .
```

---

## Managing Dependencies

```bash
# Add a production package
uv add <package-name>

# Add a development package
uv add --dev <package-name>

# Remove a package
uv remove <package-name>
```
