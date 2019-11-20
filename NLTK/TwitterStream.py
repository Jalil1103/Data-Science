#Twitter bot that pulls tweets in relatiion to what you want. 
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import matplotlib.animation as animation
from matplotlib import style
import time
import matplotlib.pyplot as plt

#twitter access information.
access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
tweets = []
class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if 'topic' in status.text.lower():
            print(status.text)
            output = open("file_path","a")
            output.write(tweet)
            output.write("\n")
            output.close()

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    
    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream