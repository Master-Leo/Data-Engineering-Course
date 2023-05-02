# Setting tables

CREATE OR REPLACE EXTERNAL TABLE brilliant-balm-379703.trips_data_all.yellow_tripdata
OPTIONS (
  format = 'parquet',
  uris = ['gs://dbt-resources/data/yellow/yellow_tripdata_2019-*.parquet', 'gs://dbt-resources/data/yellow/yellow_tripdata_2020-*.parquet']
);