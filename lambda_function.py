import boto3
import pandas as pd
import csv
import io

def lambda_handler(event, context):
    s3_client = boto3.client('s3')

    for record in event['Records']:
        # Extract bucket and key from S3 event record
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Use the extracted bucket and key in get_object
        response = s3_client.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        # Process CSV data using Pandas
        df = pd.read_csv(io.StringIO(content))

        # Add your data analysis logic here

    return {
        'statusCode': 200,
        'body': 'CSV processing completed successfully.'
    }
