import tweepy
import os
import pandas as pd
consumer_key = "s4rhp108YWPsAnFi8RnEqLsTt"
consumer_secret = "83cqf4FhvX5t9Wpopep9uUCqskUIoMvE25Snou3BLM69I9BhUg"
access_token = "1259100090-KHRyNT9ck2PGKM66rwyZphjkgEntyluhnOVPIT9"
access_token_secret = "drKs4ZnLc9UNN32qEQ3Gm9P3kUrMGXE7jAYmRazYJggRA"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# create list to append tweets to
tweets = []

# append all tweet data to list
for tweet in tweepy.Cursor(api.search, '#HudumaNumba', count=1000000).items():
    tweets.append(tweet)

# convert 'tweets' list to pandas.DataFrame
tweets_df = pd.DataFrame(vars(tweets[i]) for i in range(len(tweets)))

# define file path (string) to save csv file to
FILE_PATH = '/home/eli/Environments/Sentiment-Analysis/HudumaNumb.txt'

# use pandas to save dataframe to csv
tweets_df.to_csv(FILE_PATH)
