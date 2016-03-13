from sys import stdin, stdout
from uuid import uuid1
import json
import redis

# Connect to the diff redis db
conn = redis.Redis(db=0)

while 1:
    
    d = stdin.readline()
    # Twe use delta as the primary key
    delt = json.loads(d).get('delta')
    print delt

    conn.setex(str(uuid1()), delt, 120) #again, I used Python's unique ID generator

    print(json.dumps({'delta': delt})) #the dump is needed because it will be piped
    stdout.flush()