import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from marklogic import Client
from load_to_marklogic import load_to_marklogic


def test_real_marklogic_load():
    df = pd.DataFrame([
        {
            "order_id": "ORD_TEST_123",
            "platform": "Blinkit",
            "order_value_(inr)": 200
        }
    ])

    load_to_marklogic(df)

    ml = Client(
        "http://localhost:8000",
        digest=("khushboopadmakar", "Khushboo@2004")
    )

    doc = ml.documents.read("data.json")

    assert "ORD_TEST_123" in str(doc)

    print("✅ Data successfully found in MarkLogic")