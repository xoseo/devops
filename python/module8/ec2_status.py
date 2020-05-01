import boto3
import sys

client = boto3.client('ec2')

def switch_status(region, current_status, desired_status):

	if current_status == 'stopped' and desired_status not in ['running', 'terminated']:
		print('Only started or terminated statuses are available for stopped instances')
		sys.exit()
	elif current_status == 'terminated':
		print('You cant change status of terminated instance')
		sys.exit()

	instances = client.describe_instance_status(Filters=[{'Name': 'instance-state-name', 'Values': [current_status]}], IncludeAllInstances=True)

	for instance in instances['InstanceStatuses']:
		if not region in instance['AvailabilityZone']:
			continue

		if desired_status == 'stopped':
			client.stop_instances(InstanceIds=[instance['InstanceId']])
		elif desired_status == 'running':
			client.start_instances(InstanceIds=[instance['InstanceId']])
		elif desired_status == 'reboot':
			client.reboot_instances(InstanceIds=[instance['InstanceId']])
		elif desired_status == 'terminated':
			client.terminate_instances(InstanceIds=[instance['InstanceId']])
		print(instance['InstanceId'])

#switch_status('us-east-1', 'running', 'terminated')