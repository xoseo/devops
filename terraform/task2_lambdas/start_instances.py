import boto3

client = boto3.client('ec2')

def start_instances(event, context):
  instances = client.describe_instances(Filters=[{'Name': 'tag:test', 'Values': ['test']}, {'Name': 'instance-state-name', 'Values': ['stopped']}])
  for res in instances['Reservations']:
    for instance in res['Instances']:
      client.start_instances(InstanceIds=[instance['InstanceId']])