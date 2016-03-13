import json
import sys

# This Python script takes the posts' metadata as input from instagram.py
# and calculates the time interval between every two posts or deltas.
# Then it prints them out to be fed to redis-insert.py to be inserted
# in the in-memory database.
last = 0 #The initial value of the previous message is set to zero
while 1: # The following block runs forever and keeps reading the feed from instagram.py and calculates deltas
    line = sys.stdin.readline() # setting up reading from standard input
    d = json.loads(line) # reading feed from instagram.py
    if last == 0 : # this holds true only for the first incoming message setting last to the first timestamp
        last = float(d["time"])
        continue
    delta = abs(float(d["time"]) - float(last)) # The delta is calculated from the difference of UNIX epochs given by Instagram API
    print json.dumps({"delta":delta, "t":d["time"]}) #Then the calculated deltas are printed out to standard out to be fed to insert-redis.py
    sys.stdout.flush()
    last = float(d["time"]) #Updating the previous timestamp with the current timestamp

