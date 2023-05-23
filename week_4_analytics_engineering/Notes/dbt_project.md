# Running a dbt project in production
- > dbt cloud includes a schedular where to create jobs to run in production
- > A single job can run multiple commands
- > Jobs can be triggered manually or on schedule
- > Each job will keep a log of the runs over time
- > Each run will have the logs for each command 
- > A job could also generate documentation, that could be viewed under the run information
- > If dbt source freshness was run, the resutls can also be viewed at the end of a job

# What is COntinuous Intergration (CI)? 
- > CI is the practice of regularly merge development branches into a central repository, after which automated builds and tests are run.
- > The goal is to reduce adding bugs to the production code and maintain a more stable project.
- > dbt allows us to enable CI on pull requests 
- > Enabled via webhooks from GitHub or GitLab
- > When a PR is ready to be merged , a webhooks is recieved in dbt Cloud that will enqueue a new run of the specified job.
- > The run of the CI job will be against a temporary schema
- > No PR will be able to be merge unless the run has been completed successfully
