"""Verify the Supabase connection and list tables with row counts.

Run locally:   python -m scripts.check_supabase
Run in Docker: docker compose run --rm check-db
"""
from psycopg import sql

from database.connection import get_connection


def main() -> None:
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("select current_database(), version()")
        db, version = cur.fetchone()
        print(f"Connected to {db} ({version.split(',')[0]})")

        cur.execute(
            "select table_name from information_schema.tables "
            "where table_schema = 'public' and table_type = 'BASE TABLE' order by 1"
        )
        tables = [r[0] for r in cur.fetchall()]
        if not tables:
            print("No tables found in the public schema.")
        for t in tables:
            cur.execute(sql.SQL("select count(*) from {}").format(sql.Identifier(t)))
            print(f"  {t}: {cur.fetchone()[0]} rows")


if __name__ == "__main__":
    main()
