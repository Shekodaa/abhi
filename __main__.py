"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3, ec2

# Create an AWS resource (S3 Bucket)
bucket = s3.BucketV2('aws-s3-devops-demo')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
