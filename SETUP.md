# Setup: Docker + Supabase

## 1. Get the Supabase connection string
Ask the team for access to the Supabase project (share credentials privately, never in the repo).
Supabase dashboard -> **Connect** -> copy the **Session pooler** connection string.
Use the pooler string: the direct `db.<ref>.supabase.co` host is IPv6-only and often fails from Docker.

## 2. Configure
```bash
cp .env.example .env      # Windows PowerShell: Copy-Item .env.example .env
# paste your DATABASE_URL into .env
```

## 3. Run
```bash
docker compose run --rm check-db   # prints tables + row counts from Supabase
docker compose up --build          # API at http://localhost:8000 ; /health and /health/db
```

Without Docker: `pip install -r requirements.txt && python -m scripts.check_supabase`.

## Conventions
- Storage is Supabase (Postgres). All column names are lowercase.
- `.env` is git-ignored; only `.env.example` is committed. Secrets are never put in code or the frontend.
