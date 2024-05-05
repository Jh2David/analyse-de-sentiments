import tweepy 
import config
import pandas as pd

client = tweepy.Client(bearer_token=config.api_key)

# Search query with keywords and language filter
query = "#F1 redbull (lang:fr OR lang:en) -is:retweet -is:reply" 
max_results = 10  

tweets = client.search_recent_tweets(query=query, tweet_fields=['text'], max_results=max_results)

# Tweets conversion in Pandas DataFrame
tweet_data = []
for tweet in tweets.data:
    tweet_data.append({
        "text": tweet.text
    })
df = pd.DataFrame(tweet_data)

# Saving the DataFrame as a CSV file
df.to_csv("data/tweets.csv", index=False)
print("Données enregistrées dans tweets.csv")