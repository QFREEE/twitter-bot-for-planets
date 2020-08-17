import tweepy
import datetime

def update_tweet(newTweet):
    consumer_key = "Udxc8y4vmHV1YYbyw9Z98OFCS" 
    consumer_secret = "dJYCvElXjztLNIr2DqFvKQ9scdDD5zmsc0OKpNTjYYAEBX40vq"
    access_key = "1295232689180749824-bLvbyGd7ax29J8U56hqQDYulcgrIav"
    access_secret = "7Yz0e8aVCbPsn7JPnGYNrvQ3YSkCuQasoW3j35Y5jzLB4"

    # Authorization to consumer key and consumer secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

    # Access to user's access key and access secret 
    auth.set_access_token(access_key, access_secret) 

    # Calling api 
    api = tweepy.API(auth) 

    api.update_status('Updating using OAuth authentication via Tweepy!')

