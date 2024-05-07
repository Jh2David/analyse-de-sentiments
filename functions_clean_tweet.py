import re
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

# NETTOYAGE DES TWEETS
def clean_tweet(tweet):
    """
    Nettoie un tweet en supprimant les URL, les mentions, les hashtags et les caractères spéciaux.
    """
    # Supprimer les URL
    tweet = re.sub(r'http\S+', '', tweet)  
    # Supprimer les mentions
    tweet = re.sub(r'@\w+', '', tweet)     
    # Supprimer les hashtags
    tweet = re.sub(r'#\w+', '', tweet)     
    # Supprimer les caractères spéciaux
    tweet = re.sub(r"[^a-zA-Z0-9À-ÿ\s]", "", tweet)
    return tweet.strip()

def lower_start_fct(tweet) :
    return tweet.lower()

def lemma_fct(tweet):
    """
    Lemmatise les mots d'un tweet en utilisant le lemmatiseur de spaCy.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(tweet)
    return ' '.join([token.lemma_ for token in doc])

# TOKENISATION
def tokenize_tweet(tweet):
    return word_tokenize(tweet)

# FILTRAGE
# Filtrage des stop-words : mots inutiles
def remove_stopwords(tokens):
    """
    Supprime du tweet tous les stop-words.
    """
    stop_words = stopwords.words('french') + stopwords.words('english')
    filtered_tweets = []
    for token in tokens:
        if token not in stop_words:
            filtered_tweets.append(token)
    return filtered_tweets