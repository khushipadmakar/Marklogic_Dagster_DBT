
    
    

select
    id as unique_field,
    count(*) as n_records

from "order_quality_analytics_db"."myschema"."my_second_dbt_model"
where id is not null
group by id
having count(*) > 1


