import boto3
import os 
from dotenv import load_dotenv
load_dotenv()

session = boto3.Session(profile_name="default")

s3_resource = session.resource("s3")
s3_client =s3_resource.meta.client
bucket_name=os.getenv("BUCKET_NAME_2")


#s3_client.put_object(Bucket=bucket_name,Key="/gluescriptsetl/")

s3_resource.meta.client.upload_file("aws_glue.py",bucket_name, "gluescriptsetl/aws_glue.py")