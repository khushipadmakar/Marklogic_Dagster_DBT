# import sys
# import os
# from dotenv import load_dotenv
# load_dotenv()

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import pandas as pd
# from marklogic import Client
# from load_to_marklogic import load_to_marklogic


# def test_real_marklogic_load():
#     df = pd.DataFrame([
#         {
#             "order_id": "ORD_TEST_123",
#             "platform": "Blinkit",
#             "order_value_(inr)": 200
#         }
#     ])

#     load_to_marklogic(df)

#     ml = Client(
#         "http://localhost:8000",
#         digest=("khushboopadmakar", "Khushboo@2004")
#     )

#     doc = ml.documents.read("data.json")

#     assert "ORD_TEST_123" in str(doc)

#     print("✅ Data successfully found in MarkLogic")







import sys
import os
import pandas as pd
import pytest
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from load_to_marklogic import load_to_marklogic


@pytest.mark.integration
def test_real_marklogic_load():
    from marklogic import Client

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
        digest=(os.getenv("ML_USERNAME"), os.getenv("ML_PASSWORD"))
    )

    doc = ml.documents.read("data.json")

    # ✅ FINAL FIX (robust handling)
    first_doc = doc[0] if isinstance(doc, list) else doc

    if hasattr(first_doc, "content"):
        content = first_doc.content
    else:
        content = first_doc["content"]

    order_ids = [record["order_id"] for record in content]

    assert "ORD_TEST_123" in order_ids

    print("✅ Data successfully found in MarkLogic")