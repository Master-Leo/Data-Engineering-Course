CREATE OR REPLACE EXTERNAL TABLE brilliant-balm-379703.hw_wk_3.fhv_external_table
OPTIONS(
  FORMAT='parquet',
  URIS=['gs://week_two_bucket/data/2019/*.parquet']
)

CREATE TABLE brilliant-balm-379703.hw_wk_3.fhv_materialized_table
as(
  SELECT * FROM brilliant-balm-379703.hw_wk_3.fhv_external_table
)

