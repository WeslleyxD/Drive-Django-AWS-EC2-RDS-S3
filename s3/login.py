import boto3
from .credentials import *


def login_aws():
    session = boto3.Session(
    aws_access_key_id=AWS_SERVER_PUBLIC_KEY,
    aws_secret_access_key=AWS_SERVER_SECRET_KEY,)
            
    s3 = session.client('s3')
    
    return s3

