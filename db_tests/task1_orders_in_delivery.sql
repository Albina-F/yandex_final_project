SELECT
    c.id AS courier_id,
    COUNT(o.id) AS orders_in_delivery
FROM
    "Couriers" AS c
    LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE
    o."inDelivery" = true
GROUP BY
    c.id
ORDER BY
    orders_in_delivery DESC;