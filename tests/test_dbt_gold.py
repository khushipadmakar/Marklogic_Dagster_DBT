import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
def test_gold_table_exists():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = 'agg_order_status_summary'
        );
    """)

    exists = cur.fetchone()[0]

    assert exists == True

    cur.close()
    conn.close()