import pandas as pd
import boto3
import os
from dotenv import load_dotenv
import json

load_dotenv()


def extract_data_from_s3():
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name="ap-south-1"
        )

        bucket_name = "icebergbucketkhushi"
        file_key = "Source_Data/Ecommerce_Delivery_Analytics_New.csv"

        obj = s3.get_object(Bucket=bucket_name, Key=file_key)

        # 🔥 FIX: Direct read (no decode)
        df = pd.read_csv(obj['Body'])

        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        print("✅ Data extracted from S3 successfully")

        return df

    except Exception as e:
        print("❌ Error while reading from S3:", e)
        return None
    

def convert_df_to_json(df, output_path="data/data.json"):
    records = df.to_dict(orient="records")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=4, ensure_ascii=False)

    print(f"✅ JSON file created at {output_path}")

    return records


if __name__ == "__main__":
    df = extract_data_from_s3()
    if df is not None:
        print(df.head())
        convert_df_to_json(df)