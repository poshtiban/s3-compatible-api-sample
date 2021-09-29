from minio import Minio

# Create client with access and secret key.
client = Minio( "s3w-shakibamoshiri.s3.ir-west-1.poshtiban.com", "HLVI3EH79FZGHUU5T1SE", "5DyycegFwCz85L63nUL2mjMQHtTC3mfwZMOLdjAZ")

buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

