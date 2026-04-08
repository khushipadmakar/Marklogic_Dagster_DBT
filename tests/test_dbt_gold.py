import psycopg2
import os
import pytest
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

def test_gold_table_exists():
    """Test that dbt gold table exists. Skips if PostgreSQL is unavailable."""
    
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "postgres"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", ""),
            host="localhost",
            port="5432"
        )
    except psycopg2.OperationalError as e:
        pytest.skip(f"PostgreSQL not available: {e}")

    try:
        cur = conn.cursor()

        cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'agg_order_status_summary'
            );
        """)

        exists = cur.fetchone()[0]

        if not exists:
            pytest.fail("Gold table 'agg_order_status_summary' not found. Run 'dbt run' first.")

        cur.close()
    finally:
        conn.close()