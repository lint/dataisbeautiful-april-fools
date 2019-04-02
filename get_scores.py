#!/usr/bin/python3
import praw
from psaw import PushshiftAPI
import datetime as dt
import json

#Logging into Reddit. Fill in credentials
r = praw.Reddit()
api = PushshiftAPI(r)

#Start and End times for the comment search
start_epoch=int(dt.datetime(2019, 3, 31).timestamp())
end_epoch = int(dt.datetime(2019, 4, 2).timestamp())

#initializing data list
data = []

#Getting all comments on apirl first 2019 in r/dataisbeautiful
for comment in api.search_comments(after=start_epoch,before=end_epoch,subreddit='dataisbeautiful',limit=None):

    #Only allowing "Data." comments
    if comment.body.strip() == "Data.":

        #Adding the number of upvotes to the list
        data.append(comment.score)

        #Simple logging for progess
        if len(data) % 100 == 0:
            print (len(data))

#Saving data
with open("data.txt",'w') as f:
    f.write(json.dumps(data,indent=4,sort_keys=True))
