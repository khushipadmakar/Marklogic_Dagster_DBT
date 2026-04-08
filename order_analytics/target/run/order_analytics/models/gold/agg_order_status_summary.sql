
  
    

  create  table "order_quality_analytics_db"."myschema"."agg_order_status_summary__dbt_tmp"
  
  
    as
  
  (
    

SELECT
    platform,

    COUNT(*) AS total_orders,

    SUM("order_value_(inr)") AS total_revenue,

    AVG("order_value_(inr)") AS avg_order_value,

    SUM(CASE WHEN order_status = 'valid' THEN 1 ELSE 0 END) AS valid_orders,
    SUM(CASE WHEN order_status = 'invalid' THEN 1 ELSE 0 END) AS invalid_orders,
    SUM(CASE WHEN order_status = 'duplicate' THEN 1 ELSE 0 END) AS duplicate_orders,
    SUM(CASE WHEN order_status = 'high_value' THEN 1 ELSE 0 END) AS high_value_orders,
    SUM(CASE WHEN order_status = 'payment_failed' THEN 1 ELSE 0 END) AS payment_failed_orders,
    SUM(CASE WHEN order_status = 'late_delivery' THEN 1 ELSE 0 END) AS late_delivery_orders,
    SUM(CASE WHEN order_status = 'suspicious' THEN 1 ELSE 0 END) AS suspicious_orders

FROM "order_quality_analytics_db"."public"."fct_transformed_orders"

GROUP BY platform
  );
  