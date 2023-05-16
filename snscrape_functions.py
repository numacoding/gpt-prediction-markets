import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date, timedelta

def scrape_tweets_by_topic(topic, time_delta=2, no_of_tweets=150):
    # Creating list to append tweet data to
    attributes_container = []
    today = date.today()
    start_point = today - timedelta(time_delta)

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{topic} since:{str(start_point)} until:{str(today)}').get_items()):
        if i>no_of_tweets:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
        
    # Creating a dataframe to load the list
    tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])

    return tweets_df

