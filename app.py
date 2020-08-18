import tweepy
import datetime
import planetsUtils

def update_tweet(planet_name, week_day):
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

    tweet_format = "Good evening. Today is Good {0}. There is no news on {1}."
    try:
        api.update_status(tweet_format.format(week_day,planet_name))
    except tweepy.error.TweepError as e:
        pass

def main():
    today_planet_name = planetsUtils.getNameOfPlanet(planetsUtils.calculateIndex())
    update_tweet(today_planet_name,planetsUtils.getDayOfTheWeek())

if __name__ == "__main__":
    main()

