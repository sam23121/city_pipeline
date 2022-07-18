-- COPY (
--        select track_id,
--                 'type',
--          traveled_d,
--           avg_speed, 
--           lat, lon, 
--           speed, 
--           lon_acc, 
--           lat_acc,
--            'time'
--        from retail.user_purchase -- we should have a date filter here to pull only required date's data
-- ) TO '{{ params.user_purchase }}' WITH (FORMAT CSV, HEADER);
-- user_purchase will be replaced with /temp/user_purchase.csv from the params in extract_user_purchase_data task
CREATE DATABASE IF NOT EXISTS `city_traffic`;
CREATE TABLE IF NOT EXISTS  `objects` (
   `track_id` INT,
   `type` varchar(20),
   `avg_speed` FLOAT,
   `lat` FLOAT,
   `lon` FLOAT,
   `speed` FLOAT, 
   `lon_acc` FLOAT,
   `lat_acc` FLOAT,
   `time` FLOAT,
);
COPY objects(`track_id`, `type`,`traveled_d`, `avg_speed`, `lat`, `lon`, `speed`, `lon_acc`, `lat_acc`, `time`)
FROM ‘../../data/20181029_d1_0800_0830.csv’
DELIMITER ‘,’
CSV HEADER;