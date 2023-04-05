SELECT station_id, name FROM
    bigquery-public-data.new_york_citibike.citibike_stations
LIMIT 100;


-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `brilliant-balm-379703.dezoomcamp.external_yellow_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://week_two_bucket/data/yellow/yellow_tripdata_2019-*.parquet', 'gs://week_two_bucket/data/yellow/yellow_tripdata_2021-*.parquet']
);

-- Check yello trip data
SELECT * FROM brilliant-balm-379703.dezoomcamp.external_yellow_tripdata limit 10;

-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE brilliant-balm-379703.dezoomcamp.external_yellow_tripdata_non_partitoned AS
SELECT * FROM tbrilliant-balm-379703.dezoomcamp.external_yellow_tripdata;
  AND VendorID=1;
