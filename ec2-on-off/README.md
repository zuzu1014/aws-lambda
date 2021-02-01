# 1. Create IAM new accessment policy for ec2, cloudwatch

        {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
            },
            {
            "Effect": "Allow",
            "Action": [
                "ec2:Start*",
                "ec2:Stop*"
            ],
            "Resource": "*"
            }
        ]
        }

# 2. Create a new role using above policy

# 3. Make a lambda function

    import boto3
    region = 'ap-northeast-2'
    instances = ['your-instance-id']
    ec2 = boto3.client('ec2', region_name=region)

    def lambda_handler(event, context):
        ec2.stop_instances(InstanceIds=instances)
        print('stop your instances: ' + str(instances))



    import boto3
    region = 'ap-northeast-2'
    instances = ['your-instance-id']
    ec2 = boto3.client('ec2', region_name=region)

    def lambda_handler(event, context):
        ec2.start_instances(InstanceIds=instances)
        print('start your instances: ' + str(instances))

# 4. Add a new rule in CloudWatch

    0 16 * * ? *  // Runs every day at 16:00 PM
