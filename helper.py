import json
from sys import stdout
from time import sleep
import calculations

# Repeat the entropy and rate calculations indefinitely.
while True:
    # Use our utility functions to calculate entropy and rate.
    entropy = calculations.entropy()
    rate = calculations.rate()

    # Dump the entropy and rate to stdout and flush the stdout so we don't end
    # up with a buffer.
    print(json.dumps({'entropy': entropy, 'rate': rate}))
    stdout.flush()

    # Rest of one second. This will give us a nice smooth function for the rate
    # and entropy values.
    sleep(1)