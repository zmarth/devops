import boto3
import json

"""
if not regions_to_check:
        regions_to_check = [r['RegionName'] for r in boto3.client('ec2').describe_regions()['Regions']]

    for region in regions_to_check:
        print('Region: ', region)
    
        ec2_resource = boto3.resource('ec2', region_name = region)
        
        running_filter = {'Name':'instance-state-name', 'Values':['running']}
        instances = ec2_resource.instances.filter(Filters=[running_filter])
        
"""





import boto3

def lambda_handler(event, context):
   
    regions_to_check = []

    # Check all regions
    if not regions_to_check:
        regions_to_check = [r['RegionName'] for r in boto3.client('ec2').describe_regions()['Regions']]

    for region in regions_to_check:
        print('Region: ', region)
    
        ec2_resource = boto3.resource('ec2', region_name = region)
        
        running_filter = {'Name':'instance-state-name', 'Values':['running']}
        instances = ec2_resource.instances.filter(Filters=[running_filter])
        
        for instance in instances:
            action = 'stop' # Default action
            
            # If tag is present then extract action from it
            if instance.tags != None:
                for tag in instance.tags:
                    if tag['Key'].lower() == 'stop':
                        action = tag['Value'].lower()
            
            if action == 'stop':
                print(f'Stopping instance {instance.id}')
                instance.stop()

            else:
                print(f'Ignoring instance {instance.id}')

        stopped_filter = {'Name':'instance-state-name', 'Values':['stopped']}
        instances = ec2_resource.instances.filter(Filters=[stopped_filter])
        
        for instance in instances:
            action = 'start' # Default action
            
            # Extract action from 'sart' tag
            if instance.tags != None:
                for tag in instance.tags:
                    if tag['Key'].lower() == 'start':
                            action = tag['Value'].lower()
            if action == 'start':
                print(f'Starting instance {instance.id}')
                instance.start()

            else:
                print(f'Ignoring instance {instance.id}')


























# regions = []
# client = boto3.client('ec2')
# for region in client.describe_regions()['Regions']:
#     regions.append(region['RegionName'])
#     for region in regions:
#         ec2 = boto3.resource("ec2", region_name=region)
#         print("EC2 region is: ", region)


# # region = 'us-east-1'

# ec2 = boto3.client('ec2', region_name=region)

# def get_instance_ids(instance_names):

#     all_instances = ec2.describe_instances()
    
#     instance_ids = []
    
#     # find instance-id based on instance name
#     for instance_name in instance_names:
#         for reservation in all_instances['Reservations']:
#             for instance in reservation['Instances']:
#                 if 'Tags' in instance:
#                     for tag in instance['Tags']:
#                         if tag['Key'] == 'Name' \
#                             and tag['Value'] == instance_name:
#                             instance_ids.append(instance['InstanceId'])
                            
#     return instance_ids

# def lambda_handler(event, context):
    
#     instance_names = event["instances"].split(',')
#     action = event["action"]

#     instance_ids = get_instance_ids(instance_names)

#     print(instance_ids)

#     if action == 'Start':
#         print("Starting your instances: " + str(instance_ids))
#         ec2.start_instances(InstanceIds=instance_ids)
#         response = "Successfully started instances: " + str(instance_ids)
#     elif action == 'Stop':
#         print("Stopping your instances: " + str(instance_ids))
#         ec2.stop_instances(InstanceIds=instance_ids)
#         response = "Successfully stopped instances: " + str(instance_ids)
    
#     return {
#         'statusCode': 200,
#         'body': json.dumps(response)
#     }