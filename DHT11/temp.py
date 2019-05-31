import sys
from time import sleep
import Adafruit_DHT
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import datetime

# Parse command line parameters.
sensor=Adafruit_DHT.DHT11
pin = 4


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

keyspace = iot
tablename = keyspace+"."+cloud

#connect to a cluster
cluster = Cluster(['10.71.11.180'])
session = cluster.connect()

session.execute("CREATE KEYSPACE IF NOT EXISTS "+keyspace+" with replication={'class':'SimpleStrategy','replication_factor':1}")
print("created keyspace")

session.execute("CREATE TABLE IF NOT EXISTS "+tablename+"(timestamp text PRIMARY KEY, temperature text);")
print("created table")

while True:
    if temperature is not None:
        print('Temp={0:0.i1f} '.format(temperature))
        column1 = str(datetime.datetime.now())
        session.execute("INSERT INTO "+tablename+"(timestamp,temperature) VALUES ("+"'"+column1+"'"+","+"'"+temperature+"'"+");")
        print("created entry in table ")
        sleep(1)
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)

