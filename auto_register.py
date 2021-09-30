import json
import boto3

def lambda_handler(event, context):
    trigger_instance = str(event['detail']['instance-id'])
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        for tag in instance.tags:    
            if (tag['Key']) == 'Env':
                if (tag['Value']) == 'Dev' :
                    if trigger_instance == str(instance.id):
                        print(instance.id)
                        client = boto3.client('elbv2')
                        response = client.register_targets(
                            TargetGroupArn='arn:',
                            Targets=[
                                {
                                    'Id': trigger_instance,
                                    'Port': 80,
                                },
                            ],
                        )  
                        print(response)
                
