# What is deployment?
- > Process of running the models we created in our development environment in a production environment
- > Development and later deployment allows us to continue building models and testing them without affecting oru productio nenvironment
- > A deployment environment will normally have a different schema in our data warehouse and ideally a different user
- > A development - deployment workflow will be something like:
    - Develop in a user branch
    - Open a PR to merge into the main branch
    - Merge the branch to the main branch
    - Run the new models in the production environemnt using the main branch
    - Schedule the models 

# * Production Environmnet *
(1) Development Environment
(2) Develop
(3) Test and document 
(4) Deployment (Version control and CI/CD)

