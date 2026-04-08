from dagster import job
from .ops import run_extract,run_tests, run_transform, run_load, run_dbt

@job
def etl_pipeline():
    extract = run_extract()
    run_tests()
    transform = run_transform()
    load = run_load()
    dbt_result = run_dbt()
    