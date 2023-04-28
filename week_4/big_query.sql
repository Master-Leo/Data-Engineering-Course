# Setting tables

CREATE OR REPLACE EXTERNAL TABLE brilliant-balm-379703.trips_data_all.yellow_tripdata
OPTIONS (
  format = 'parquet',
  uris = ['gs://week_two_bucket/data/yellow/yellow_tripdata_2019-*.parquet', 'gs://week_two_bucket/data/yellow/yellow_tripdata_2020-*.parquet']
);