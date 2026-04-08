from dagster import job
from .ops import run_extract, run_transform, run_load, run_dbt,run_tests

@job
def etl_pipeline():
    extract = run_extract()
    transform = run_transform()
    load = run_load()
    dbt_result = run_dbt()
    run_tests()