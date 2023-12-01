import os
import boto3
import pandas as pd

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Download the file from S3
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    csv_content = response['Body'].read().decode('utf-8')

    # Use Pandas to read the CSV content into a DataFrame
    df = pd.read_csv(pd.compat.StringIO(csv_content))

    # Now you can use df as needed
    print(df)
    print('Done processing the file!')
