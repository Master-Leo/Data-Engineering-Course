# What is dbt?
- > Dbt is a transformation tool that allows anyone that knows SQL to deploy analytics code following software engineering best practice 
    - > like modularity, portability, Continuous Integration/Continuous Deployment/Delivery, and documentations 

# How does dbt work? 
- > Each model is:
    - A *.sql file
    - Select statements, no DDL or DMl
    - A file taht dbt will compile and run in our DWH 

# Into to dbt
- > dbt Core
    - Open-source project that allows the data transformation
    - Builds and runs a dbt project (.sql and .yml files) 
    - includes SQL compilations logic, macros and databases adapters
    - Includes a CLI interface to run dbt commands locally 
    - Opens sources and free to use 

- > dbt Cloud
    - SaaS application to develop and manage dbt projects
    - Web-based IDE to develop, run and test a dbt project 
    - Jobs orchestration
    - Logging and Alerting 
    - Integrated documentation
    - Free for individuals (one developer seat) 

# How will we execute dbt?
- > BigQuery
    - Development using cloud IDE
    - No local installation of dbt core

- > Postgres
    - Development using a local IDE of your choice.
    - Local installation of dbt core connecting to the postgres database
    - Running dbt models through the CLI
