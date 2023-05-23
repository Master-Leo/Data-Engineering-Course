# Setting tables

CREATE OR REPLACE EXTERNAL TABLE brilliant-balm-379703.trips_data_all.yellow_tripdata
OPTIONS (
  format = 'parquet',
  uris = ['gs://dbt-resources/data/yellow/yellow_tripdata_2019-*.parquet', 'gs://dbt-resources/data/yellow/yellow_tripdata_2020-*.parquet']
);


--create fhv data cluster table 
CREATE OR REPLACE EXTERNAL TABLE brilliant-balm-379703.trips_data_all.fhv_tripdata_clustered
OPTIONS (
  format = 'parquet',
  uris = ['gs://dbt-resources/data/2019/fhv_tripdata_2019-*.parquet', 'gs://dbt-resources/data/2020/fhv_tripdata_2020-*.parquet']
);