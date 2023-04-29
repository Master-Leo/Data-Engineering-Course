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


# Anatomy of a dbt model
- > {{
        config(materialized='table') --> Several materialization strategies include: 'Table, View, Incremental, Ephemeral' 
    }}

- > Sequence:
    1) dbt model
        - model.sql 
            --> Compiled Code
                --> Runs compiled code in the data warehouse   

- > The FROM clause of a dbt model
* Sources * 
    - The data loaded to our dwh that we use as sources for our models
    - Configuration defined in the yml files in the models folder 
    - Used with the source macro that will resolve the name to the right schema, plus build the dependencies automatically
    - Source freshness can be defined and tested
* Seeds *
    - CSV files stored in our repository under the seed folder
    - Benefits of version controlling 
    - Equivalent to a copy command 
    - Recommended for data that doesn't change frequently
    - Runs with dbt seeds -s file_name 
* Ref *
    - Macros to reference the underlying tables and vies that were building the data warehouses
    - Run the same code in any environment, it will resolve the correct schema for you
    - Dependencies are build automatically 

# Macros 
    - Use control structure (e.g. if statements and for loops) in SQL
    - Use environment variables in your dbt project for production deployments
    - Abstract snippets in SQL into reusable macros -- these are analogous to functions in most programming languages

# Packages
    - Like libraries in other programming languages
    - Standalone dbt project, with models and macros that tackle a specific problem area
    - By adding a package to your project, the package's models and macros will become part of your own project
    - Imported in the packages.yml file and imported by running dbt deps
    - A list of useful packages can be find in dbt package hub

# Variables
    - Variables are useful for defining values that should be used across the project
    - With a macro, dbt allows us to provide data to models for compilation
    - To use a variable we use the { { var ('..') }} functin
    - Variables can defined in two ways:
        - In the dbt_project.yml file 
        - On the command line 