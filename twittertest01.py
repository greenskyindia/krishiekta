#!/usr/local/bin/python

import twitter
from twitter import *


# see "Authentication" section below for tokens and keys

OAUTH_TOKEN = '1428538422-MicTgeg9Zktp4BDq7p3v2vvcDMZa7CRVfXFcNKh'
OAUTH_SECRET = '0kPANMGh0nO8TJO4IwJr4SUhKkyubtE8DgANXXIqc'
CONSUMER_KEY = 'bIxtXeixZeZPHeIbJLbgA'
CONSUMER_SECRET = 'wcH44EQYzbzhcSk3KldSit6UH2vdd12liTfByFp4jc'

t = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )

# Get your "home" timeline
#a = t.statuses.home_timeline()

#f = open('data001/twit01.json','w')

#f.write(a)

# Get a particular friend's timeline
#t.statuses.friends_timeline(id="greenskyindia")

# Also supported (but totally weird)
#t.statuses.friends_timeline.billybob()

# Update your status
#t.statuses.update(status="Testing automated tweet no. 3 for KrishiEkta v1.0")

# Send a direct message
t.direct_messages.new(
    user="greenskyindia",
    text="i-Shakti Dals are unpolished and have not been damaged by artificial stone powder, colour or oil that are used by others to polish dals.")

# Get the members of tamtar's list "Things That Are Rad"
#t._("tamtar")._("things-that-are-rad").members()

# Note how the magic `_` method can be used to insert data
# into the middle of a call. You can also use replacement:
#t.user.list.members(user="tamtar", list="things-that-are-rad")

# An *optional* `_timeout` parameter can also be used for API
# calls which take much more time than normal or twitter stops
# responding for some reasone
#t.users.lookup(screen_name=','.join(A_LIST_OF_100_SCREEN_NAMES), _timeout=1)


# Search for the latest tweets about #pycon
#b = t.search.tweets(q="#NutritionAtGS")


#print(b)
#x = twitter.statuses.home_timeline()

# The first 'tweet' in the timeline
#print("\t",x[0])

# The screen name of the user who wrote the first 'tweet'
#print("\t\t",x[0]['user']['screen_name'])
