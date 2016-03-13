import redis
import json
import time
import sys

# This Python scripts essentially looks into the stored values in redis
# and calculates the rate of the messages.
# If the interval between messages falls below 1 minute (rate<=60 seconds)
# an alert is generated and fed to the web interface.
conn = redis.Redis() #connection to redis made

while 1: #this loop will run forever, storing key-value pair of posts and calculating the rate of messages

    pipe = conn.pipeline() # Connection is made and a pipeline is established
    keys = conn.keys() # Getting the keys (that are posts)
    values = conn.mget(keys) #Here, keys are the posts

    try:
        # This block prints the deltas or the interval between two messages/posts
        deltas = [float(v) for v in values]
    except TypeError:
        # Troubleshoot block
        continue

    #the following if-else block calculates the actual rate of messages/posts
    if len(deltas): #this checks if delta is not 0. If it is non-zero, we calculate the rate
        rate = sum(deltas)/float(len(deltas)) #We get the rate by dividing the number of messages by the total time interval of those messages
        #if(rate<=60):
            # Here we check if we have a rate less than or equal to 60 seconds.
            # The 60 seconds is the set threshold for my system.
            # If posts are coming in with #fire and #nyc hashtags more frequently than 60 seconds
            # I am posting an alert for fire in NYC
            # print json.dumps({"rate":rate})
            # sys.stdout.flush()
            print "Alert! Alert! Possible Fire in New York City!"
        sys.stdout.flush()
    else:
        rate = 0 #As per the first if statement, if the number of delta is zero we assign rate to zero

    

    time.sleep(2)