import redis
import sys
from sys import stdin
import json
from uuid import uuid1


# This script inserts the distribution information of the system in db=1 of redis
conn = redis.Redis(db=1)


while True:
    line = sys.stdin.readline()
    try:
        d = json.loads(line)
    except ValueError:
        # do oothing
        continue

    try:
        hashtag = d["hashtag"]
    

    randomNum = str(uuid1()) #we are using Python's random unique id generator here for the primary key of the DB
    conn.setex(str(uuid1()), hashtag, 90) #90 seconds was chosen based on observation + trial-n-error
    print json.dumps({"UID":randomNum, "hashtag":hashtag})
    sys.stdout.flush()
