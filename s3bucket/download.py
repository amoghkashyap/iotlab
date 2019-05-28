from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,BucketAlreadyExists)
from datetime import timedelta
import time
import sys

startTime = time.clock()

access = sys.argv[1]
secret = sys.argv[2]
bucket = sys.argv[3]
data = sys.argv[4]
path = sys.argv[5]

print(sys.argv)
minioClient = Minio('10.71.11.180:9000',access_key=access,secret_key=secret,secure=False)


# Get a full object
try:
    minioClient.fget_object(bucket,data,path)
    print(minioClient.fget_object(bucket,data,path))
except ResponseError as err:
    print(err)

# presigned get object URL for object name, expires in 2 days.
try:
    print(minioClient.presigned_get_object(bucket,data,path, expires=timedelta(days=7)))
# Response error is still possible since internally presigned does get bucket location.
except ResponseError as err:
    print(err)


endTime = time.clock()
timeTaken = endTime - startTime
print("total time taken to read = ", timeTaken)


