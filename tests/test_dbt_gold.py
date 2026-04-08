import psycopg2

def test_gold_table_exists():
    conn = psycopg2.connect(
        dbname="order_quality_analytics_db",
        user="postgres",
        password="Khushboo@2004",
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