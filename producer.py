import boto3

region_name='us-west-2'

sqs = boto3.resource('sqs', region_name)

print(sqs)

