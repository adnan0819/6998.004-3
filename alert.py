from time import sleep
from sys import stdin, stdout
from datetime import datetime
import json
import json
from time import sleep
import calculations

# This is where we set our rate threshold. The process for deriving it is
# described in the comments above.
RATE_THRESHOLD = 100

ENT_THRESHOLD = 0.2 

while True:
   
    entropy = calculations.entropy()
    rate = calculations.rate()

    print entropy

        # Dump the entropy and rate to stdout and flush the stdout so we don't end
        # up with a buffer.
    
        # Rest of one second. This will give us a nice smooth function for the rate
        # and entropy values.
 

    # This is a variable that will keep track of whether the system is currently
    # in an anomalous period or not. This is the main mechanism for preventing
    # duplicate messages during a period of time with anomalous behavior.
    uncommonRate=False
    uncommonEntropy=False


    # Read in the input from stdin, which is a JSON with a key 'avg' containing
    # the average for the values in the DB (which have been there for < 120
    # seconds)
    
    # Now, if we find that the current average is less than the threshold,
    # we are experiencing anomalous behavior.
    if entropy > ENT_THRESHOLD :
        # This is entered when the previous reading was not anomalous.
            uncommonEntropy=True
            print "System is slowing down and tags are becoming uniform. Possible calamity alert!"
            # As always, make sure to flush the stdout to prevent Python from
            # keeping a buffer.
            stdout.flush()
            uncommonEntropy=False
            sleep(3)


    