# Index

1. OLAP vs OLTP
-- Online Transaction Processing:
    -> Purpose:
        - Control and run essential bussines operations in real time
    -> Data Updates:
        - Short, fast updates initiated by user
    -> Database Design:
        - Normalized databases for efficiency
    -> Space Requirements:
        - Generally smal lif historical data ia archived 
    -> Backup and Recovery:
        - Regular backups required to ensure business continuity and meet legal and governance requirements 
    -> Productivity: 
        - Increases productivity of end users
    -> Data view:
        - Lists day-to-day business transactions
    -> User Examples:k
        - Customer-facing personnel, clerks, online shoppers 

-- Online Analytical Processing:
    -> Purpose:
        - Plan, solve problems, support decisions, discover hidden insights
    -> Data Updates:
        - Data periodically refreshed with scheduled, long-running batch jobs
    -> Database Design:
        - Denormalized databases for analysis 
    -> Space Requirements:
        - Gernally large due to aggregating datasets 
    -> Backup and recover:
        - Lost data can be reloaded from OLTP database as needed in lieu of regular backups
    -> Productivity:
        - Increases productivity of business manageers, data analysts, and executives
    -> Data View:
        - Mult-dimensional view of enterprise data
    -> User examples:
        - Knowledge works such as data analysts, business analysts, and executives 

2. What is data warehouse
- An OLAP Solution
- Used for reporting and data analysis 
    -> Consists of Meta Data, Summary Data, Raw Data

3. BigQuery
-> Serverless data warehouse
    - There are no servers to manage or database software to instal
-> Software as well as infrastrucutre including 
    - Scalability and High-Availability
-> Built in features like
    - Machine Learning
    - Geospatial analysis
    - Business intelligence
-> BigQuery maximizes flexibility by separating the compute engine that analyzes your data from your storage 

Take-away points: 
    - Cost
    - Partitions and Clustering 
    - Best practices
    - Internals
    - ML in BQ