#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "732577785751838720-URNB2NxwZASCPwHRZPEsvApsA4FHeRw"
access_token_secret = "zx2QqtmwIvCUmNksq3Y60ydZ2HSXgGC496rYunLG3ZY50"
consumer_key = "3NbaUbPKzrhKzbv0DtX56zbkp"
consumer_secret = "lNUUnP8vOnedVhisQK74QXP0smXpsc2wn9Mj9O0QSkxr3eJFzM"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'unifree'
    stream.filter(track=['utd', 'dallas', 'free', 'food'])