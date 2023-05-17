
# Maximizing Confiden in Data Model Changes and Dbt/PipeRider 

# Whats the problem?
- > Why we need a a better Pull Request process
    - Large and complex dbt projects
    - Large scale datasets are difficutl to understand 

- > When making data model changes
    - Difficult to assess the impact 
    - Errors make it into production 

# Current Methods
- > How do you check the data?
    - > Eyeballing the data - or running 'random queries' 
    - > BI Tools - Not ideal, the data should be ready by the time it reaches BI tools. No easy way to copare development and production data
    - > Dbt tests - Powerful, but you need to write the tests. Signal to noise issue with many tests. 

# What is PipeRider
- > Open-Source data profiling toolkit 
- > Improved 'code review for data projects' in dbt 

- > Features:
    - Open-Source CLI tool:
        - Data profiler
        - Data profile reports (HTML)
        - Data profile comparison
        - Multiple data connectors available
        - Integration with dbt 
        - Data assertions 

# Data Profiler
- > Data
    - > Data exploration - understand data
    - > Data quality analysis
    - > Discover hidden data (outliers, weird values)
    - > Suitabel for large datasets
    - > Easy to digest and share a profile report (without building first a dashboard)
     
# Using PipeRider in your data project
- > Developing and testing data models locally 
    - Engineers creating and modifying data models locally
- > Deploying model changes
    - Reviewing changes submitted by pull request to existing projects
    - Taps into the vision controlled nature of dbt projects
    - Automated as part of Continuous Integration process 


# Basic (local) workflow
- > Create a branch
- > Install PipeRider
- > Initialize PipRider
- > dbt build
- > Run PipeRide (initial report)
- > Update data models
- > dbt build
- > Run PipRider (second report)
- > Compare reports
- > Pull Request with comparison summary


# Continuous Integration
- > Why CI with data projects?
    - > Automate tasks on a software project
        - > Building, testing, linting
    - > Ensures quality (no more merging buggy code)
    - > Data projects are now full 'software projects'
    - > Data projects should take advantage of the automation CI brings 