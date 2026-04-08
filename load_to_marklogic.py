
import json
import pandas as pd
from dotenv import load_dotenv
from marklogic import Client
from marklogic.documents import Document
from source_data_extract import convert_df_to_json
import os

load_dotenv()

def load_to_marklogic(df):
    print("🚀 Starting MarkLogic load process...")

    # Connect to MarkLogic
    ml = Client(
        "http://localhost:8000",
        digest=(os.getenv("ML_USERNAME"), os.getenv("ML_PASSWORD"))
    )

    print("✅ Connected to MarkLogic")

    # Step 1: Convert DataFrame → list of records
    records = convert_df_to_json(df)
    print(f"📦 Records extracted: {len(records)}")

    # Step 2: Convert list → JSON string
    json_string = json.dumps(records)
    print("🔄 Converted records to JSON string")

    # Step 3: Write to MarkLogic
    doc = Document("data.json", json_string)
    result = ml.documents.write(doc)

    print("✅ Data successfully loaded into MarkLogic")
    print("📄 Response:", result)


if __name__ == "__main__":
    print("📂 Loading JSON file...")

    # ✅ Correct Windows path (IMPORTANT: use raw string)
    json_path = r"C:\Users\HP\Downloads\MarkLogic\data\data.json"

    # ✅ Read JSON (NOT CSV)
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    print("📊 DataFrame loaded")
    print(df.head())

    load_to_marklogic(df)