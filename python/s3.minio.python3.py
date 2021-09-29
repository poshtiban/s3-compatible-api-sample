from minio import Minio

# Create client with access and secret key.
# Please update endpoint, access-key-secret-key, this credentials are dummy!
client = Minio( "s3w-shakibamoshiri.s3.ir-west-1.poshtiban.com", "t7XViGJK3LaKMhj9", "q7lfyrT5qMHgsCle2DJzUtajsm5xvJrz" )

buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

