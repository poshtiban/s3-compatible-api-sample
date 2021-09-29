import boto
import boto.s3.connection

# Please update endpoint, access-key-secret-key, this credentials are dummy!
access_key = 't7XViGJK3LaKMhj9'
secret_key = 'q7lfyrT5qMHgsCle2DJzUtajsm5xvJrz'
endpoint   = 's3w-shakibamoshiri.s3.ir-west-1.poshtiban.com'

s3 = boto.connect_s3(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,
    host = endpoint,
    #is_secure=False,               # uncomment if you are not using ssl
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

for bucket in s3.get_all_buckets():
    print( bucket.name,bucket.creation_date )
