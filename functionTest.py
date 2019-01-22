import boto3
import argparse
import tests

parser = argparse.ArgumentParser(description='Input the IP I need')
parser.add_argument('--BUILD_ID', required=True)
args = parser.parse_args()

build_id = str(args.BUILD_ID).lower()


cf = boto3.client('cloudformation', region_name='us-east-2')
response = cf.describe_stacks(StackName='demoStack' + build_id)
new_ip = response['Stacks'][0]['Outputs'][1]['OutputValue']

tests.test_app(new_ip)
