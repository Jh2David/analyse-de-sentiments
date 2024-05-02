import tweepy 
import pandas as pd

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAABHvtQEAAAAAZYZuSyP3Xt5GNPVE8SDaFL8km%2FE%3DHWxI0NcvZzQYB28eJummwmZ8zfb20lLBMHkpzERg4oLF9tFktq")

# Search query with keywords and language filter
query = "#F1 redbull (lang:fr OR lang:en) -is:retweet -is:reply" 
max_results = 10  

tweets = client.search_recent_tweets(query=query, tweet_fields=['text'], max_results=max_results)

# Conversion des tweets en DataFrame Pandas
tweet_data = []
for tweet in tweets.data:
    tweet_data.append({
        "text": tweet.text
    })
df = pd.DataFrame(tweet_data)

# Enregistrement du DataFrame dans un fichier CSV
df.to_csv("data/tweets.csv", index=False)
print("Données enregistrées dans tweets.csv")