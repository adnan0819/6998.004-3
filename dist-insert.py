# insert-distribution.py
# Jonah Smith
# Assignment 3, Storytelling with Streaming Data, Spring 2016
#
# This script takes a pipe from stdin, in which every message is a JSON
# corresponding to a single edit on english Wikipedia. It extracts the city name
# and puts that into a Redis database (running on the default port) as the
# value of an entry. (The key is a randomly generated unique identifier.)
#
# Entries are set to expire after 15 minutes. This time seems like a good scale
# for Wikipedia edits, because minute-to-minute there might be too much noise to
# get a good sense of the distribution, but anything longer than about half an
# hour would fail to capture the variations we are interested in (like a bot or
# a burst of activity in response to some major event), which could happen at a
# scale less than fifteen minutes. Fifteen minutes allows us to observe some
# variation without being a slave to random noise.

import redis
import sys
from sys import stdin
import json
from uuid import uuid1


# Establish a Redis connection on the default port, but with db index 1. This
# will allow us to separate the distribution database from the database
# containing time diffs (which is used to calculate the rate).
conn = redis.Redis(db=1)

# This variable is going to hold all of the categories we have seen before.
# That's important so that we can put one entry in the DB that will never erase
# (since we know there is always a non-zero probability of that category
# existing).

# Repeat indefinitely...
while 1:
    line = sys.stdin.readline()
    try:
        d = json.loads(line)
    except ValueError:
        # sometimes we get an empty line, so just skip it
        continue

    try:
        hashtag = d["hashtag"]
    except KeyError:
        # if there is no city present in the message
        # then store a "null" city
        hashtag = "null"

    t = str(uuid1())
    conn.setex(str(uuid1()), hashtag, 5)
    print json.dumps({"UID":t, "hashtag":hashtag})
    sys.stdout.flush()
