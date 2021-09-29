from minio import Minio
import os

# Create client with access and secret key.
client = Minio( os.environ['END_POINT'], os.environ['ACCESS_KEY'], os.environ['SECRET_KEY'] )

buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

