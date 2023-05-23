import io
import os
import requests
import pandas as pd
from google.cloud import storage

"""
Pre-reqs: 
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

# services = ['fhv','green','yellow']
init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'
# switch out the bucketname
BUCKET = os.environ.get("GCP_GCS_BUCKET", "dbt-resources")


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


def web_to_gcs(year, service):
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name
        file_name = f"{service}_tripdata_{year}-{month}.csv.gz"

        # download it using requests via a pandas df
        request_url = f"{init_url}{service}/{file_name}"
        r = requests.get(request_url)
        open(f'./data/{service}/{file_name}', 'wb').write(r.content)
        print(f"Local: {file_name}")

        df = pd.read_csv(f'./data/{service}/{file_name}', compression='gzip')
        # green_cols = ['trip_distance', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'ehail_fee', 'improvement_surcharge', 'total_amount','congestion_surcharge']
        # yellow_cols = ['trip_distance','fare_amount', 'extra','mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge','total_amount', 'congestion_surcharge']
        if service == 'yellow':
            df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
            df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
            # df[yellow_cols] = df[yellow_cols].apply(pd.to_numeric, errors='coerce')
            df['VendorID'] = df['VendorID'].astype(float)
            df['fare_amount'] = df['fare_amount'].astype(float)
            df['passenger_count'] = df['passenger_count'].astype(float)
            df['payment_type'] = df['payment_type'].astype(float)
            df['RatecodeID'] = df['RatecodeID'].astype(float)
        else:
            df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
            df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])
            # df[green_cols] = df[green_cols].apply(pd.to_numeric, errors='coerce')
            df['VendorID'] = df['VendorID'].astype(float)
            df['fare_amount'] = df['fare_amount'].astype(float)
            df['passenger_count'] = df['passenger_count'].astype(float)
            df['payment_type'] = df['payment_type'].astype(float)
            df['RatecodeID'] = df['RatecodeID'].astype(float)
            df['trip_type'] = df['trip_type'].astype(float)

        
        # read it back into a parquet file
        file_name_parquet = file_name.replace('.csv.gz', '.parquet')
        df.to_parquet(f'./data/{service}/{file_name_parquet}', engine='pyarrow')

        print(df.head(2))
        print(f'columns: {df.dtypes}')
        print(f'rows: {len(df)}')
        
        print(f"Parquet: {file_name_parquet}")

        # upload it to gcs 
        upload_to_gcs(BUCKET, f'data/{service}/{file_name_parquet}', f'./data/{service}/{file_name_parquet}')
        print(f"GCS: {file_name_parquet}")

        # remove the csv.gz file
        os.remove(f'./data/{service}/{file_name}')
        os.remove(f'./data/{service}/{file_name_parquet}')
        print(f"Removed: {file_name}")
        print(f"Removed: {file_name_parquet}")


web_to_gcs('2019', 'yellow')
web_to_gcs('2020', 'yellow')
# web_to_gcs('2019', 'yellow')
# web_to_gcs('2020', 'yellow')
