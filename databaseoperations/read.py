from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement


cluster = Cluster(['10.71.11.180'])
session = cluster.connect()

data = session.execute("select * from workshop.student_entries;")

for entry in data:
    print("data ", entry)
    print("team name: '%s'      team value : '%s'"%(entry.teamname,entry.status))
