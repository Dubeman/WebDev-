import tweepy
from dotenv import load_dotenv
import os
load_dotenv()
# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
bearer_token = os.getenv('BEARER_TOKEN')

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = os.getenv('TWITTER_API_KEY')
consumer_secret = os.getenv('TWITTER_API_SECRET')

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# You can authenticate as your app with just your bearer token
client = tweepy.Client(bearer_token=bearer_token)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
# Fetch the 5 most recent tweets from your timeline
tweets = client.get_users_tweets(id=client.get_me().data.id, max_results=5)

# Print each tweet's text
for tweet in tweets.data:
    print(tweet.text)