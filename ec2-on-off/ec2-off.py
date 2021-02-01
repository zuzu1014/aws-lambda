    import boto3
    region = 'ap-northeast-2'
    instances = ['your-instance-id']
    ec2 = boto3.client('ec2', region_name=region)

    def lambda_handler(event, context):
        ec2.stop_instances(InstanceIds=instances)
        print('stop your instances: ' + str(instances))