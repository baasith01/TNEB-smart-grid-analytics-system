SELECT

r.region_name,

ROUND(
SUM(m.units_consumed),0
) AS total_units,

w.avg_temperature,

w.avg_humidity,

w.total_rainfall

FROM meter_readings m

JOIN consumers c

ON m.consumer_id = c.consumer_id

JOIN regions r

ON c.region_id = r.region_id

JOIN weather_summary w

ON r.region_name = w.city

GROUP BY

r.region_name,

w.avg_temperature,

w.avg_humidity,

w.total_rainfall

ORDER BY total_units DESC;

SELECT

city,

avg_temperature,

total_rainfall

FROM weather_summary

ORDER BY avg_temperature DESC;

SELECT

city,

total_rainfall

FROM weather_summary

ORDER BY total_rainfall DESC;