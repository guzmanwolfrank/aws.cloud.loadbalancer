import boto3

# Create an ELBv2 client
elbv2_client = boto3.client('elbv2')

# Create a load balancer
response = elbv2_client.create_load_balancer(
    Name='my-load-balancer',
    Subnets=['subnet-12345678'],
    SecurityGroups=['sg-12345678']
)

# Get the DNS name of the load balancer
load_balancer_dns_name = response['LoadBalancers'][0]['DNSName']

# Register a target group with the load balancer
response = elbv2_client.create_target_group(
    Name='my-target-group',
    Protocol='HTTP',
    Port=80,
    VpcId='vpc-12345678',
    HealthCheckProtocol='HTTP',
    HealthCheckPort='traffic-port',
    HealthCheckPath='/health-check'
)

# Get the target group ARN
target_group_arn = response['TargetGroups'][0]['TargetGroupArn']

# Register a target with the target group
response = elbv2_client.register_targets(
    TargetGroupArn=target_group_arn,
    Targets=[
        {
            'Id': 'i-12345678'
        }
    ]
)
