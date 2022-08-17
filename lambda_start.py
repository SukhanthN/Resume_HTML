import boto3
region = 'us-east-1'
instances = ['i-03d2341f9ba7e9823', 'i-0253c9bd715c5164e']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))