
Intro: 
CREATE OR REPLACE EXTERNAL TABLE brilliant-balm-379703.hw_wk_3.fhv_external_table
OPTIONS(
  FORMAT='parquet',
  URIS=['gs://week_two_bucket/data/2019/*.parquet']
)

CREATE TABLE brilliant-balm-379703.hw_wk_3.fhv_materialized_table
as(
  SELECT * FROM brilliant-balm-379703.hw_wk_3.fhv_external_table
)

Question 1:
SELECT COUNT(*) 
FROM brilliant-balm-379703.hw_wk_3.fhv_materialized_table 

answer: 43,244,696

Question 2:
SELECT COUNT(distinct affiliated_base_number)
FROM brilliant-balm-379703.hw_wk_3.fhv_external_table 
-- estimated bytes 0 MB bc not stored in BQ external table unlike materialized table 315 MB 

Question 3:
SELECT COUNT(*)
FROM brilliant-balm-379703.hw_wk_3.fhv_materialized_table
WHERE PUlocationID is null and DOlocationID is null 

answer: 71,7748

Question 4:
--Best strategy to optimized the table if query always filter by pickup_datetime and order by affiliated_base_number?
-> Partition by pickup_datetime Cluster on affiliated_base_number 

Question 5:
SELECT distinct affiliated_base_number
FROM brilliant-balm-379703.hw_wk_3.fhv_partitioned_table
WHERE pickup_datetime between '2019-03-01' and '2019-03-31'

-- 23 MB used in partitioned table instead of 647 MB in materialized table 

Question 6: 
-- Where is the data stored in the External Table you created?
-> GCP bucket 

Question 7:
-- It is best practice in BQ to always cluster you data:
-> FALSE  
    - LESS THAN 1GB creates metadata and outweights cluster benefits 

Question 8: 