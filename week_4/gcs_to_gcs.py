import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Define a function to write a Pandas DataFrame to a Parquet file
def write_modified_parquet(df, output_file):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, output_file)

# Define the GCS bucket and directory 
bucket_name = 'dbt-resources'
directory = 'data/green/'

# Loop through the 12 months and retrieve the data from GCS then Upload back to GCS
for month in range(1, 13):
    # Construct the GCS URL for the current month's data
    dataset_url = f'gs://{bucket_name}/{directory}green_tripdata_2019-{month:02}.parquet'
    
    df = pd.read_parquet(dataset_url)
    
    df['trip_type'] = df['trip_type'].astype(float)
    
    output_url = f'gs://{bucket_name}/{directory}green_tripdata_2019-{month:02}.parquet'
    
    write_modified_parquet(df, output_url)
    
    print(f'Processed month: {month}, uploaded to: {output_url}')
