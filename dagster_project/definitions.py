from dagster import Definitions
from .jobs import etl_pipeline

defs = Definitions(
    jobs=[etl_pipeline]
)