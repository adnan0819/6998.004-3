from sys import stdout
import requests
import json
import time
import sys
import datetime  
reload(sys)  
sys.setdefaultencoding('utf-8') 

# In this Python Script, I am polling the Instagram API every two seconds
# to monitor the hashtags (#flood, #snow, #hurricane, #rain, #earthquake) and their locations.
# For the convenience of demo purposes, I have included #food, #selfie and #l4l
# that are the most common hashtags.
# The warning message from the API is natural because we are not using OAuth
# or else you would have to log in using your Instagram ID
# For best results, wait about 5 minutes to see meaningful output.

tagId=0
tagFoodId=0 #these counts are used as flags so we do not repeat the same row twice
tagSnowId=0
tagRainId=0
tagStormId=0
tagSelfieId=0
tagFloodId=0
tagHurricaneId=0
tagL4lId=0
tagFireId=0
tagEarthquakeId=0
tagFoodIdPrev=-1 #this is a placeholder for a food hashtag that stores the "previous" post's ID to avoid repetition
tagSnowIdPrev=-1
tagRainIdPrev=-1
tagStormIdPrev=-1
tagSelfieIdPrev=-1
tagFloodIdPrev=-1
tagHurricaneIdPrev=-1
tagL4lIdPrev=-1
tagEarthquakeIdPrev=-1
tagFireIdPrev=-1



while True:
    #This is the infinite loop to call the "recent tags" endpoint of Instagram API
    r = requests.get("https://api.instagram.com/v1/tags/latergram/media/recent?access_token=186174857.3d82e12.e8205e331f0a47499a1e4008c3b86f3b")
    for m in r.json()["data"]:


            tagId=m["id"] #this is the ID of the specific post

            # The following if statements search for the substring of "food"
            # in the hashtag array
            # STRENGTH: In the following if-blocks since we are using substings
            # we can get a match for "raining" or "flooding" even if we test
            # for "rain" or "flood" respectively
            # from these filtered posts, we extract the date, location, longitude and latitude
            # Any image without geolocation is discarded
                             
            if any("food" in s for s in m["tags"]):                        
                                    print json.dumps({"hashtag": "food", "time": m["created_time"]}) 
                                    stdout.flush()
                                    tagFoodIdPrev=tagFoodId #Assigning this particular post to "previous" id because we are done with it. 

                                    #THE SAME LOGIC CONTINUES FOR THE FOLLOWING IF-ELSE BLOCKS (for different hashtags)
            if any("fire" in s for s in m["tags"]):

                                
                                    tagFireId=m["id"]
                                    print json.dumps({"hashtag": "fire", "time": m["created_time"]}) 
                                    stdout.flush()
                                    tagFireIdPrev=tagFireId #Assigning this particular post to "previous" id because we are done with it. 

                                    #THE SAME LOGIC CONTINUES FOR THE FOLLOWING IF-ELSE BLOCKS (for different hashtags)
                                               
            if any("hurricane" in s for s in m["tags"]):

                                   
                                    tagEarthquakeId=m["id"]
                                    print json.dumps({"hashtag": "hurricane", "time": m["created_time"]}) 
                                    stdout.flush()
                                    tagHurricaneIdPrev=tagHurricaneId

            if any("earthquke" in s for s in m["tags"]):

                                
                                    print json.dumps({"hashtag": "earthquake", "time": m["created_time"]}) 
                                    stdout.flush()
           
            if any("flood" in s for s in m["tags"]):

                                
                                    print json.dumps({"hashtag": "flood", "time": m["created_time"]}) 
                                    stdout.flush()
                                    tagFloodIdPrev=tagFloodId
            
                                
            if any("rain" in s for s in m["tags"]):
                               
                                    print json.dumps({"hashtag": "rain", "time": m["created_time"]}) 
                                    stdout.flush()
                                   
                                
            if any("snow" in s for s in m["tags"]):

                              
                                    print json.dumps({"hashtag": "snow", "time": m["created_time"]}) 
                                    stdout.flush()

                                   
            if any("storm" in s for s in m["tags"]):

                                
                                    print json.dumps({"hashtag": "storm", "time": m["created_time"]}) 
                                    stdout.flush()
                                    
                                
            if any("selfie" in s for s in m["tags"]):

                               
                                    print json.dumps({"hashtag": "selfie", "time": m["created_time"]}) 
                                    stdout.flush()
                                    
            if any("l4l" in s for s in m["tags"]):

                                
                                    print json.dumps({"hashtag": "l4l", "time": m["created_time"]}) 
                                   
                                    stdout.flush()
            
    

    time.sleep(2)
 