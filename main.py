import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



# # AWS Credentials
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_ACCESS_SECRET_ID")
REGION = os.getenv("AWS_REGION")  # e.g., 'us-east-1'
INSTANCE_ID = os.getenv("AWS_INSTANCE_ID")  # Replace with your EC2 instance ID

print(REGION)

# # Initialize the EC2 client with credentials
# ec2 = boto3.client(
#     "ec2",
#     aws_access_key_id=AWS_ACCESS_KEY,
#     aws_secret_access_key=AWS_SECRET_KEY,
#     region_name=REGION
# )

# def start_instance():
#     response = ec2.start_instances(InstanceIds=[INSTANCE_ID])
#     print(f"Starting instance: {INSTANCE_ID}")
#     return response

# def stop_instance():
#     response = ec2.stop_instances(InstanceIds=[INSTANCE_ID])
#     print(f"Stopping instance: {INSTANCE_ID}")
#     return response

# # Uncomment the function you want to execute
# # start_instance()
# # stop_instance()

