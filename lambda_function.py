import pandas as pd

def lambda_handler(event, context):
    # Assuming the CSV file content is in the 'Records' field of the S3 event
    s3_event = event['Records'][0]['s3']
    bucket_name = s3_event['bucket']['name']
    object_key = s3_event['object']['key']

    # Use Boto3 to download the CSV file from S3
    import boto3
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    csv_content = response['Body'].read().decode('utf-8')

    # Use Pandas to read the CSV content into a DataFrame
    df = pd.read_csv(pd.compat.StringIO(csv_content))

    # Now you can use df as you would in your original lambda_handler function
    print(df)
    print('Done x1')
