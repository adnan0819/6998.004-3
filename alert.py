from time import sleep
from sys import stdin, stdout
from datetime import datetime
import json
import json
from time import sleep
import calculations

# I have set up the threshold for the distribution as 1.5 because in most cases we see that
# it is around 0.2 to 1.0 across the visible tags (10 in total). However it should be noted that
# sometimes, some tags do not show up like "fire" or "earthquake" - leading to a more uniform distribution 
# i.e. lower entropy. As we move higher and uncommon ones come in, we will see the entropy go high because
# even though the selfie type hashtags will dominate, there will be few #fire, #earthquake etc. 
# consequently this will give rise to the entropy Based on this idea, I have made the alerting system
# that outputs in stdout and also the web page. 

THRESH = 1.5 #the entropy threshold

while True:
   
    entropy = calculations.entropy() #using helper script for calculation
     
    uncommonEntropy=False #this is a flag so that once we find an alert we do not loop through it. We will switch it to false again in the end.
    
    if entropy > THRESH :
            uncommonEntropy=True #  making the flag true now
            print "System is slowing down and tags are becoming uniform. Possible calamity alert!"
            stdout.flush()
            uncommonEntropy=False #after the alert is done, we switch back.
            sleep(3) #I picked 3 seconds to sleep


    