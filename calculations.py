import redis
import json
from collections import Counter
from math import log

rate_conn = redis.Redis(db=0)
dist_conn = redis.Redis(db=1)


def histogram():
    keys = dist_conn.keys()
    bins = dist_conn.mget(keys)
    while not all(bins):
        keys = dist_conn.keys()
        bins = dist_conn.mget(keys)
    counts = Counter(bins)
    total = len(bins)
    hist={bin: count/float(total) for bin, count in counts.items()}
    
    data=[]

    for tag, count in counts.items():
        item = {"bin": tag}
        item["count"] = count/float(total)
        
        data.append(item)
    
    jsonData=json.dumps(data)
    print jsonData
    return jsonData
    #return json.dumps(data)
    
    #return hist


def rate():
    keys = rate_conn.keys()
    deltas = rate_conn.mget(keys)
    #print deltas
    while not all(deltas):
        keys = rate_conn.keys()
        deltas = rate_conn.mget(keys)
    deltas = [float(delta) for delta in deltas]
    avg = sum(deltas)/len(delta)
    return avg


def entropy():
    keys = dist_conn.keys()
    bins = dist_conn.mget(keys)
    while not all(bins):
        keys = dist_conn.keys()
        bins = dist_conn.mget(keys)
    counts = Counter(bins)
    total = len(bins)
    hist={bin: count/float(total) for bin, count in counts.items()}
    #print hist
    entropy = -sum( [p*log(p) for p in hist.values()] )
    return entropy


def probability(tag):
    keys = dist_conn.keys()
    bins = dist_conn.mget(keys)
    while not all(bins):
        keys = dist_conn.keys()
        bins = dist_conn.mget(keys)
    counts = Counter(bins)
    total = len(bins)
    hist={bin: count/float(total) for bin, count in counts.items()}
    prob = hist.get(tag, 0)
   
    return prob