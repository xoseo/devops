import boto3

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')

    table = client.Table("task6_s3-event")
    filename = event['Records'][0]['s3']['object']['key']
    md5 = event['Records'][0]['s3']['object']['eTag']
    table.put_item(Item= {'file_name': filename, 'md5_sum': md5})
