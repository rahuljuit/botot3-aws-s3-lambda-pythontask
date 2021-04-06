import json
import urllib
import boto3

# boto3 S3 initialization
s3_client = boto3.client("s3")



def lambda_handler(event, context):
    destination_bucket_name = 'tech-output-bucket'

   # event contains all information about uploaded object
    print("Event :", event)

   # Bucket Name where file was uploaded
    source_bucket_name = event['Records'][0]['s3']['bucket']['name']

   # Filename of object (with path)
    file_key_name = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

   # Copy Source Object
    copy_source_object = {'Bucket': source_bucket_name, 'Key': file_key_name}

    try:
        waiter=s3_client.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket_name,Key=file_key_name)
    # S3 copy object operation
        s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=file_key_name)

    except Exception as e:
        print(e)
        print('Error while trying to copy the file. does not exist'.format(file_key_name,soure_bucket_name))
        raise e