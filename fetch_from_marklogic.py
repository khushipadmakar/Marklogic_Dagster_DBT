import requests
import pandas as pd
from sqlalchemy import create_engine
from requests.auth import HTTPDigestAuth
import os
from dotenv import load_dotenv
from dotenv import load_dotenv
load_dotenv()

# -------------------------------
# PostgreSQL Connection
# -------------------------------
engine = create_engine(
    "postgresql://postgres:Khushboo%402004@localhost:5432/order_quality_analytics_db"
)

# -------------------------------
# Fetch Data from MarkLogic
# -------------------------------
def fetch_transformed_data(uri):
    url = f"http://localhost:8000/v1/documents?uri={uri}&format=json"
    
    response = requests.get(
        url,
        auth=HTTPDigestAuth(os.getenv("ML_USERNAME"), os.getenv("ML_PASSWORD"))
    )

    print(f"\nFetching: {uri}")
    print("STATUS:", response.status_code)

    if response.status_code != 200:
        print(response.text)
        raise Exception("❌ Failed to fetch data")

    data = response.json()

    # If your document is stored as JSON array directly
    if isinstance(data, list):
        df = pd.json_normalize(data)
    else:
        # If wrapped inside a document node
        df = pd.json_normalize(data.get("envelope", data))

    return df

# -------------------------------
# Load into PostgreSQL
# -------------------------------
def load_to_postgres(table_name, uri):
    try:
        df = fetch_transformed_data(uri)

        print(f"Loading {table_name}... Rows: {len(df)}")

        df.to_sql(table_name, engine, if_exists="replace", index=False)

        print(f"✅ Loaded {table_name}")

    except Exception as e:
        print(f"❌ Error: {e}")

# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":

    # 🔥 Your transformed document URI
    load_to_postgres("fct_transformed_orders", "transformed-data.json")

    print("\n🎉 DONE!")