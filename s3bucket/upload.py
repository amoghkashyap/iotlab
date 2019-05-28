from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,BucketAlreadyExists)
import time
import sys

startTime = time.clock()
access = sys.argv[1]
secret = sys.argv[2]
bucket= sys.argv[3]
data = sys.argv[4]
path = sys.argv[5]


print(sys.argv)
minioClient = Minio('10.71.11.180:9000',access_key=access,secret_key=secret,secure=False)

try:
       minioClient.make_bucket(bucket, location="us-east-1")
except BucketAlreadyOwnedByYou as err:
       pass
except BucketAlreadyExists as err:
       pass
except ResponseError as err:
       raise

# Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
try:
	   minioClient.fput_object(bucket,data,path)
	   print("writing to bucket")
except ResponseError as err:
	   print(err)
endTime = time.clock()
timeTaken = endTime - startTime
print("total time taken to write = ", timeTaken)

