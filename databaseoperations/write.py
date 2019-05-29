from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import sys

#connect to a cluster
cluster = Cluster(['10.71.11.180'])
session = cluster.connect()

keyspace = sys.argv[1]
tablename = keyspace+"."+sys.argv[2]
column1 = sys.argv[3]
column2 = sys.argv[4]



session.execute("CREATE KEYSPACE IF NOT EXISTS "+keyspace+" with replication={'class':'SimpleStrategy','replication_factor':1}")
print("created keyspace")

session.execute("CREATE TABLE IF NOT EXISTS "+tablename+"(teamName text PRIMARY KEY, status text);")
print("created table")


session.execute("INSERT INTO "+tablename+"(teamname,status) VALUES ("+"'"+column1+"'"+","+"'"+column2+"'"+");")
print("created entry in table ")
