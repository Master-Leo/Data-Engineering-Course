# Introduction to Batch Processing
- > Batch vs Streaming  -- 80% / 20%
- > Types of batch jobs
- > Orchestration batch jobs
- > Advantages and disadvantages of batch jobs

-- > Batch - processing a chunck of data at regualr intervals. 
-- > Stream - processing data on the fly 

# Types of batch jobs:
- > SQL, Pythong Scripts, Spark, Flink

# Advantages:
- > easy to manage
- > retry, scale: easier to orchestrate 

# Disadvantage:
- > delay 



# Spark introduction
- > What is Spark?
    - > Spark:
    - > A 'general purpose distributed processing engine' 
    - > Common use cases: batch-type workloads. 
        - > Also, streaming, but we won't cover it here

- > Why do we need it 
    - > Same processes as SQL - but for executing the queries on the files in your datalake 



# When to use Spark?
- > In a datalake (S3/GCS: parquet) -> SPARK(SQL) -> DL
    - > May use Hive/Presto/Athena in DL to execute SQL before exporting back into DL 
 