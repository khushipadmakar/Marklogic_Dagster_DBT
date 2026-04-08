-- Use the `ref` function to select from other models

select *
from "order_quality_analytics_db"."myschema"."my_first_dbt_model"
where id = 1