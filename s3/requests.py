import boto3
from pathlib import Path
from .login import login_aws
from .credentials import BUCKET

s3 = login_aws()

def list_all_items_by_user(user):
    items = s3.list_objects(Bucket=BUCKET, Prefix=f'{user}/').get('Contents', '')
    all_items = [item['Key'].replace(f'{user}/', '') for item in items]
    return all_items

def delete_item_user(key):
    s3.delete_object(Bucket=BUCKET, Key=key)
    return True

def download_item_user(key, name):
    path = Path.home() / "Downloads"
    s3.download_file(Bucket=BUCKET, Key=key, Filename=f'{path}/{name}')

def validate_limit_storage(user, file, limit_storage=25000000):
    items = s3.list_objects(Bucket=BUCKET, Prefix=f'{user}/').get('Contents', '')
    storage = sum([item['Size'] for item in items])

    sum_storage_now = storage+file

    if storage <= limit_storage and sum_storage_now <= limit_storage:
        return True
    else:
        return None

def storage(user, limit_storage=25000000):
    items = s3.list_objects(Bucket=BUCKET, Prefix=f'{user}/').get('Contents', '')
    storage = sum([item['Size'] for item in items])

    percent_storage = round((storage/limit_storage) * 100, 1)
    
    return percent_storage