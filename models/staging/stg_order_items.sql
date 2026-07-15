SELECT
    order_id,
    product_id,
    seller_id,
    price
FROM {{ source('olist', 'order_items') }}
