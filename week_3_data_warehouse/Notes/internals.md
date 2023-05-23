# BigQuery Architecture

- > Dremal: the compute part of BQ. Executes SQL queries in bits.
    (1) Dremal responsible for SQL queries turning into execution trees. The leaves are referred to as 'Slots' and the branches are called 'Mixers'. 
    (2) The slots read data from storage then perform calculations.
    (3) The branches aka 'Mixers' responsible for aggegrations.
    (4) Dremal handles apportion slots to queries when needed, maintaining fairness for concurrent queries for x-amount of users.

- > Colossus: Google's global storage system.
    (1) BQ leverages a ~Columnar storage format~ and compression algorithms to store data.
    (2) Optimized for reading large scale structured data.
    (3) Handles replications as well, recovery and distributed management.

- > Jupiter: The network that connects Dremel and Colossus. 
    (1) Created by Google utilized for interconnecting its datacenters.

- > Borg: an orchestration solution that handles everything
    (1) A precursor of Kubernetes.