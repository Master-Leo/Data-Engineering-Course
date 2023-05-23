# BigQuery-Best Practice

1. Cost Reduction
    - > Avoid SELECT *
        - Specifiy specific columns instead 
    - > Price your queries before running them
    - > Use clustered or partitioned tabels
    - > Use streaming inserts with caution
        - May increase cost drastically 
    - > Materialize query results in stages 
        - When using CTE's 

2. Query performance
    - > Filter on partioned columns
    - > Denormalizing data 
    - > Use nested or repeated columns
    - > Use external data sources appropriately 
    - > Dont use it, in case you want a high query performance
    - > Reduce data before using a JOIN
    - > Do not treate WITH clauses as prepared statements
    - > Avoid oversharding tables 

        (1) Avoid JavaScript user-defined functions
        (2) Use approximate aggregation functions (HyperLogLog++)
        (3) Order Last, for query operations to maxime performance
        (4) Optimize your join patterns
        (5) As a best practice, place the table with the largest number of rows first, followed by the table with the fewest rows, and then place the remaining tables by decreasing size 