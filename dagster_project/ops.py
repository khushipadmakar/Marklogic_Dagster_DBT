from dagster import op
import os

@op
def run_extract():
    print("Running extraction...")
    os.system("python source_data_extract.py")

@op
def run_transform():
    print("Running transform...")
    os.system("python fetch_from_marklogic.py")

@op
def run_load():
    print("Running load...")
    os.system("python load_to_marklogic.py")

@op
def run_dbt():
    print("Running dbt models...")
    os.system("cd order_analytics && dbt run")



@op
def run_tests():
    print("🧪 Running pytest tests...")

    # Run all tests
    exit_code = os.system("pytest -v")

    if exit_code != 0:
        raise Exception("❌ Pytest failed")

    print("✅ All tests passed successfully")