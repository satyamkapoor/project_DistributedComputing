# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:59:31 2017

@author: vase & Satyam
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
        if i < 20000:
            if status.lang == 'en':     #we need only English language
                    if status.place.country == 'United States':     #filter for USA
                        f = open("tweets.txt", "a") 
                        try:
                            f.write((status.text.replace('\n', '')).encode("utf8")) #saving text parameter & stripping of \n which might have been added by the user
                        except AttributeError:
                            print ('error -- ') #Witnessed an instance of Attribute error, purposely declared to know it it existed
                            
                        f.write("\n") #as we've already stripped of \n now adding \n to the end of each tweet (text)
                        f.close()
                        for hashtag in status.entities['hashtags']: 
                            f = open("hashtags.txt", "a") 
                            try:
                                f.write(hashtag['text'].encode("utf8")) #saving hashtags
                            except:
                                raise
                            f.write("\n")
                            f.close()
                        i = i + 1
                    else: #because there is no geo, we don't save tweets for other countries
                        err = err + 1 #Don't feel there's a need of this but need to confirm once from Vase about it.
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