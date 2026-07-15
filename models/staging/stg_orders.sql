SELECT
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp AS order_ts
FROM {{ source('olist', 'orders') }}
