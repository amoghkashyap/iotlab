from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement


cluster = Cluster(['10.71.11.180'])
session = cluster.connect()

keyspace = 'workshop'

session.execute("""CREATE KEYSPACE IF NOT EXISTS %s with replication={'class':'SimpleStrategy','replication_factor':1}""" %keyspace)
print("created keyspace")

session.execute('CREATE TABLE IF NOT EXISTS workshop.student_entries(teamName text PRIMARY KEY, status text);')
print("created table")

session.execute("INSERT INTO workshop.student_entries(teamname,status) VALUES ('second entry','success');")
print("created entry in table ")
