# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:59:31 2017

@author: vase_
"""

import sys
import tweepy


access_key = "940968924467945472-pcTOE0Lo6fHt8AWyHy7o5KKCdQDQhIA"
access_secret = "5UBUgQmAJpmTgaNMvNsAMcJzvBgoY2lKtfYdKTrGnW24u"
consumer_key = "PQOm1uKmBRrJkXoqiqTEctNjs"
consumer_secret = "VMhE8IZzNJdq9wZrha861dx6a7nfQ36UzO65WN5FLVUaupbBb5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    global i    #variable for counting saved tweets
    global err  #variable for not USA countries
    i = 0
    err = 0
    def on_status(self, status):
        global i
        global err
        if (i < (20000+err)):
            if status.lang == 'en':     #we need only English language
                    if status.place.country == 'United States':     #filter for USA
                        f = open("text3.txt", "a") 
                        try:
                            f.write(status.text.encode('utf-8')) #saving only text parameter
                        except: 
                            #print "error"
                            raise
                        f.write("\n")
                        f.close()
                        for hashtag in status.entities['hashtags']: 
                            f = open("hashtags3.txt", "a") 
                            try:
                                f.write(hashtag['text'].encode('utf-8')) #saving hashtags
                            except:
                                #print "error"
                                raise
                            f.write("\n")
                            f.close()
                        #print i
                        i = i + 1
                        #print "--------"
                    else: #because there is no geo, we don't save tweets for other countries
                        err = err + 1
                        #print "error", err
        else:
            sys.exit()

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True #Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True #Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    #create Stream
sapi.filter(locations=[-122.995004, 32.323198, -67.799695, 49.893813]) #limit only for USA
