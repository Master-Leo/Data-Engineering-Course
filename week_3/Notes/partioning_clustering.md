1. BigQuery Partiion
    (1) Time-unit Column
    (2) Ingestion time (_PARTITIONTIME)
    (3) Integer range partitioning 
    (4) When using Time unit or ingstion time
        - Daily (Default)
        - Hourly 
        - Monthly or yearly 
    (5) Number of partitions limit is 4000 

2. BigQuery Clustering 
    (1) Columns you specify are used to colocate related data
    (2) Order of the column is important 
    (3) The order of the specified columns determines the sort order of the data.
    (4) Clustering improves
        - Filter queries 
        - Aggregate queries
    (5) Table with data size < 1 GB, don't show significant improvement with partitioning and clustering 
    (6) You can specify up to four clustering columns 

3. BigQuery Clustering 
    -> Clustering columns must be top-level, non-repeated columns
        - Date
        - Bool
        - Geography 
        - Int64
        - Numeric
        - BigNumeric
        - String 
        - Timestamp
        - Datetime 

4. What is the difference between Partitioning vs Clustering
    -> Clustering:
        - Cost benefit unknown
        - You need more granularity than partioining alone allows
        - Your queries commonly use filters or aggregation against multiple particular columns 
        -The cardinality of the number of values in a column or gorup of columns is large
    -> Partioning 
        - Cost known upfront
        - You need partition-level management
        - Filter or aggregate on single column 

5. Clustering over partioning
    -> Partioning results in a small amount of data per partition (approximately less than 1GB)
    -> Partioning results in a large number of partitions beyond the limits on partioned tables
    -> Partitions in the table frequently (for example, every few minutes)

6. Automatic reclustering
    -> As data id added to a clustered table
        - The newly inserted data can be written to blocks that ocntian key ranges that overlap with the key ranges in prevously written blocks
        - These overlapping keys weaken the sort property of the table 
    -> To mainttain the performance characteristics of a clustered table 
        - BigQuery perform automatic re-clustering in the background to restore the sort property of the table
        - For partiioned tables, clustering is maintained for data within the scope of each partition1