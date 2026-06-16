select count(*) as total_regions from regions;
select count(*) as total_transformers from transformers;
select count(*) as total_consumers from consumers;
select count(*) as total_meter_readings from meter_readings;

select consumer_type, count(*) as total_consumers from consumers group by consumer_type order by total_consumers desc;

select status, count(*) as total from consumers group by status;

select consumer_id, sum(units_consumed) as total_units from meter_readings group by consumer_id order by total_units desc limit 10;

select c.region_id, r.region_name, sum(m.units_consumed) as total_units from meter_readings m join consumers c on m.consumer_id = c.consumer_id join regions r on c.region_id = r.region_id group by c.region_id, r.region_name order by total_units desc;

select transformer_id, region_id, health_score, failure_count from transformers where health_score < 70 order by health_score asc;

CREATE TABLE weather_summary (

city VARCHAR(50),

avg_temperature DECIMAL(5,2),

avg_humidity DECIMAL(5,2),

total_rainfall DECIMAL(10,2),

avg_wind_speed DECIMAL(5,2)

);

select * from weather_summary;