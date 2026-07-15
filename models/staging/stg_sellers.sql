SELECT
    seller_id,
    seller_city
FROM {{ source('olist', 'sellers') }}
