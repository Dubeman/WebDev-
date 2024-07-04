import tweepy
import os
from dotenv import load_dotenv
load_dotenv()


# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
bearer_token = os.getenv("BEARER_TOKEN")

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


client = tweepy.Client(bearer_token)

# Get Tweets

# This endpoint/method returns a variety of information about the Tweet(s)
# specified by the requested ID or list of IDs

tweet_ids = [1460323737035677698, 1293593516040269825, 1293595870563381249]

# By default, only the ID and text fields of each Tweet will be returned
# Additional fields can be retrieved using the tweet_fields parameter
response = client.get_tweets(tweet_ids, tweet_fields=["created_at"])

for tweet in response.data:
    print(tweet.id, tweet.created_at)