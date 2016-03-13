# COMSE6998.004 Assignment 3

# Calamity Alert Powered by Instagram 

# - Adnan Firoze (af2728)
# (Dual MS in CS & Journalism)


As sugested in previous assignment(s), I am using the Instagram API's streaming "recent posts" to triangulate major calamities as opposed to popular culture tags like #selfie or #food. 

This project/assignment polls Instagram API's ***recent tags endpoint*** and pulls out "#fire", "#hurricane", "#rain", "#snow", "#flood", "#food", "#selfie", "#l4l" and "#earthquake" tags appearing together. From there, we calculate the distribution, rate, entropy, to shed light on narratives not only for calamities but Instagram's growing popularity in journalism (See next section for background).

# Why should one care in journalism?

Firstly it has been shown by multiple media outlets that social media has become an extremely efficient means of storytelling. For instance, www.journalism.co.uk pointed out the efficacy of USA's Electiongram and Stormgram that were very effective in the past few years. In their report (https://www.journalism.co.uk/news/-how-bbc-guardian-innovating-instagram/s2/a555771/) they argued that more and more citizen journalists are turning to instagram for breaking news coverage as both consumers and content creators. 

Also, Niemen Labs pointed out the 91 years old lonform narrative journalism magazine - "Virginia Quarterly Review" has found its unique place in Instragram. 

So, I attempted to find and triangulate fires, rain, snow etc. along with trivially popular tags like selfie and food to measure and track if we can find unlikely events when a specific important calamity like "fire" takes over "selfies." 

# The Data

The stream I selected is the Instagram recently uploaded hashtag stream from the API endpoint: https://api.instagram.com/v1/tags/latergram/media/recent?access_token=186174857.3d82e12.e8205e331f0a47499a1e4008c3b86f3b .
Note that the access token is mine. 


**What each message mean?**

Every message polled from this refers to the event of a person taking a picture of a specific fire event (at this moment) that relates to the hashtags mentioned. Note that I used a subsring search so even if I am searching for "fire" I will get hashtags like "buidingfire", "firestorm" etc. Same is true for earthquake, snow, flood and unfortunately selfies. 


**The nitty-gritty of the codes are well comprehensively commented in the source files**

# Files of Relevance

1. instagram.py (the stream)
2. delta.py (measures the time intervals between messages)
3. redis-insert.py (inserts deltas into redis)
4. dist-insert.py (inserts distribution into redis - I used two DBs)
5. api.py (the API endpoint implementation using Flask)
6. script2.js (the d3 visualization)
7. calculations.py (a helper function to calculate entropy, rate, propabilities etc.)
8. alert.py (the alerting script)
9. index.html (frontend implementing BOTH the distribution and alerting system)

# How to run:

**Prerequisites:** 

- ` Python 2.7x `
- ` Redis `
- ` Requests ` 
- ` Websocketd `
- ` Flask ` 


**Running the API powered Frontend**

Assuming you are using a Mac (or any UNIX based terminal) and have the prerequisites (Python 2.7, websocketd) installed the steps are as follows:

1. Download this directory to your computer

2. In the terminal, change to the directory to the directory where the files have been downloaded.

3. I used Python 2.7 (it will not work properly in Python 3.x). Simply type ` python instagram.py | tee >(python delta.py | python redis-insert.py) >(python dist-insert.py) ` and hit enter. It saves time because it parallelly pipes to multiple processes. 

4. Make sure Redis is running (if not running, type in "redis-server" in Terminal assuming it is in the path). 

5. Then in a different terminal tab (while point 1 is running) type in ` python api.py ` and hit enter. Now we have the API ready and one could use it in web application and also CURL using the URL: http://127.0.0.1:5000/

Example:

>> curl http://127.0.0.1:5000/histogram

Output: "[{"bin": "food", "count": 0.5}, {"bin": "fire", "count": 0.25}, {"bin": "selfie", "count": 0.25}]"

So here 'bins' are the hashtags and counts are self-explanatory (frequency of occurence every 2 minutes)

Another example of the API is necessary as it takes a GET parameter as follows:

>>http://127.0.0.1:5000/probability?tag=selfie

Output: {"p": 0.5, "tag": "selfie"}

6. While in the directory in the terminal type ` python -m SimpleHTTPServer ` .  Now we are good to go as we have this directory serving over port 8000. 

6. Open up Chrome and browse to ` localhost:5000 ` to find a visualization of the distribution (made in D3), the raw distribution and also the alerting system.


**Alerts**

1. Although we are all set uo for distribution, the alert is not ready yet. A little more work is necessary. 

2.In a different terminal tab (with everything running from the previous section), type ` websocketd --port 8080 python alert.py `

3. And that's it. We don't need a different web page because the index.html has a button that will start the alert on the same page as the distribution from the same link as above i.e. ` localhost:5000 ` .


**Alert Parameters and Why I used Entropy (SIGNIFICANCE)**

 I have set up the threshold for the distribution as 1.5 because in most cases we see that it is around 0.2 to 1.0 across the visible tags (10 in total). However it should be noted that sometimes, some tags do not show up like "fire" or "earthquake" - leading to a more uniform distribution  i.e. lower entropy. As we move higher and uncommon ones come in, we will see the entropy go high because even though the selfie type hashtags will dominate, there will be few #fire, #earthquake etc. consequently this will give rise to the entropy Based on this idea, I have made the alerting system that outputs in stdout and also the web page. 

**Extra Note**

Note that my implementation of histogram is different from the one shown in class.This is because I needed a format like {{bin:flood,count:2}, {bin:selfie, count:120}} unlike the one in class where it would be {{flood,2},{selfie,120}}. This is to facilitate the D3 visualization. 