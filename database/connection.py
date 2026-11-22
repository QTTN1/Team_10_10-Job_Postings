"""Shared Supabase (Postgres) connection helper. Reads DATABASE_URL from the environment/.env."""
import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection() -> psycopg.Connection:
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL is not set. Copy .env.example to .env and fill it in.")
    return psycopg.connect(url, connect_timeout=10)
