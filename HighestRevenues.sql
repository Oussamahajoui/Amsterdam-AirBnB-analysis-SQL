
SELECT id,
    listing_url,
    name,
    365 - availability_365 AS booked_out_365,
    CAST(REPLACE(Price, '$', '') AS UNSIGNED) AS price_clean,
    CAST(REPLACE(Price, '$', '') AS UNSIGNED) *(365 - availability_365) / beds AS proj_rev_365
FROM listings
ORDER BY proj_rev_365 DESC
LIMIT 100;