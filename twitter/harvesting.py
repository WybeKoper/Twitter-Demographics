# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import csv
import time
# Enter Twitter API Keys
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

twts = []
# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
                #f.write(data)
                print(data)
                time.sleep(10)
                #twts.append(data)
                return
        except BaseException as e:
            #print("Error on_data: %s" % str(e))
            return

    def on_error(self, status):
        #print(status)
        return

    def on_exception(self, exception):
        #print(exception)
        return

if __name__ == '__main__':
    with open('10CandidatesFullName22.json', 'a') as f:
        # Handle Twitter authetification and the connection to Twitter Streaming API
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=['Bernie', 'Sanders', 'Elizabeth', 'Warren', 'Andrew','Yang', 'Joe', 'Biden', 'Pete','Buttigieg', 'Tom','Steyer' ,'Cory', 'Booker', 'Amy', 'Klobuchar', 'Mike', 'Bloomberg', 'Tulsi','Gabbard'], languages=["en"], stall_warnings=True)
