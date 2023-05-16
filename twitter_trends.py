import tweepy
import os
import json
import sys
import geocoder
import pandas as pd
from snscrape_functions import scrape_tweets_by_topic


# API Keys and Tokens
twitter_api_key = os.environ['API_KEY']
twitter_secret_key = os.environ['API_SECRET_KEY']
twitter_bearer_token = os.environ['BEARER_TOKEN']
no_of_tweets = 100

# Authorization and Authentication
auth = tweepy.OAuth2BearerHandler(twitter_bearer_token)
api = tweepy.API(auth)


def get_trends(api, loc):
    # Object that has location's latitude and longitude.
    g = geocoder.osm(loc)
    closest_loc = api.closest_trends(g.lat, g.lng)
    trends = api.get_place_trends(closest_loc[0]["woeid"])
    return trends[0]["trends"]

trends = get_trends(api, 'New York')

final_df = pd.DataFrame()
for trend in trends[:20]:
    if trend['name'][0] != '#':
        trend_name = trend['name']
        print(f'Working on trends: {trend_name}')
        try:
            #The number of tweets we want to retrieved from the search
            tweets = api.search_tweets(q=trend_name, count=no_of_tweets)
            
            #Pulling Some attributes from the tweet
            attributes_container = [[tweet.created_at, tweet.favorite_count, tweet.text] for tweet in tweets]

            #Creation of column list to rename the columns in the dataframe
            columns = ["Date Created", "Number of Likes", "Tweet"]
            
            #Creation of Dataframe
            tweets_df = pd.DataFrame(attributes_container, columns=columns)

            tweets_df['Trend'] = trend


        except BaseException as e:
            print('Status Failed On,',str(e))

        pd.concat([final_df, tweets_df], ignore_index=True)
    else:
        pass

print(final_df.head(10))



#next steps
## tweet translation
## keep the main words
## send it to the GPT prompt

