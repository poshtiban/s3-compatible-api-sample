import boto
import boto.s3.connection
import os

access_key = os.environ['ACCESS_KEY']
secret_key = os.environ['SECRET_KEY']
endpoint   = os.environ['END_POINT']

s3 = boto.connect_s3(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,
    host = endpoint,
    #is_secure=False,               # uncomment if you are not using ssl
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

for bucket in s3.get_all_buckets():
    print( bucket.name,bucket.creation_date )
