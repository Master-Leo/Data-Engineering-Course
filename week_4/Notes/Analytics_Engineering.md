# Data Domain Developments
1) Massively paralletl processing (MPP) databases
2) Data-Pipelines-as-services
3) SQL-First
4) Version control systems
5) Self service analytics
6) Data Governance 

# Roles in a Data Team
- > Data Engineer:
    - Prepares and maintain the infrastrucutre the data team needs. 

# Tooling 
1) Data Loading
2) Data Storing: 'Cloud data warehoues like Snowflake, BigQuery, Redshift'
3) Data modeling: 'Tools like DBT or Dataform'
4) Data presentation: 'BI Toolds like google data studio, Looker, Mode, or Tableau

# Data Modelling concepts 
## ETL vs ELT
1) Extract(Sources) -> Transform -> Load(Data Warehouses) -> Reporting
    - Slightly more table and compliant data analysis 
    - Higher storage and compute costs'

2) Extract(Sources) -> Load/Transform(Data Warehouses) -> Reporting 
    - Faster and more flexible data analysis
    - Lower cost and lwoer maintenance 

# Kimball's Dimensional modeling 
- > Objective 
    - Deliver data understandable to the business users
    - Deliver fast query performance
- > Approach
    - Prioritise user understandability and query performance over non redundant data (3NF) 
- > Other approaches
    - Bill Inmon
    - Data Vault 

# Elements of Dimensional Modeling 
- > Facts tables
    - Measurements, metrics or facts
    - Corresponds to a business process 
    - 'Verbs'

- > Dimensions tables
    - Corresponds to a business *entity* 
    - Provides context to a business process
    - 'Nouns' 

# Architecture of Dimensional Modeling
- > Stage Area
    - Contains the raw data 
    - Not meant to be exposed to everyone 
- > Processing area
    - From raw data to data models
    - Focuses in efficiency
    - Ensuring standards 
- > Presentation area
    - Final presentation of the data
    - Exposure to business stakeholder

