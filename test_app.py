import unittest
from unittest.mock import patch
from functions_clean_tweet import clean_tweet, lower_start_fct, lemma_fct, tokenize_tweet, remove_stopwords

def test_clean_tweet():
    test_tweet = "This is a sample tweet with #hashtag and @mention. https://example.com"
    cleaned_tweet = clean_tweet(test_tweet)
    assert "http" not in cleaned_tweet
    assert "#" not in cleaned_tweet
    assert "@" not in cleaned_tweet
    assert "example.com" not in cleaned_tweet

def test_lower_start_fct():
    test_tweet = "This is a sample tweet with #hashtag and @mention. https://example.com"
    lowered_tweet = lower_start_fct(test_tweet)
    assert lowered_tweet == "this is a sample tweet with #hashtag and @mention. https://example.com"

@patch('spacy.load')
def test_lemma_fct(mock_spacy_load):
    mock_model = unittest.mock.Mock()
    mock_model.return_value = [unittest.mock.Mock(lemma_='sample'), unittest.mock.Mock(lemma_='tweet')]
    mock_spacy_load.return_value = mock_model
    test_tweet = "This is a sample tweet with #hashtag and @mention."
    lemmatized_tweet = lemma_fct(test_tweet)
    assert lemmatized_tweet == "sample tweet"


def test_tokenize_tweet():
    test_tweet = "This is a sample tweet with #hashtag and @mention."
    tokens = tokenize_tweet(test_tweet)
    assert isinstance(tokens, list)
    assert "tweet" in tokens

def test_remove_stopwords():
    tokens = ["this", "is", "a", "sample", "tweet", "with", "hashtag", "and", "mention"]
    filtered_tokens = remove_stopwords(tokens)
    assert "a" not in filtered_tokens
    assert "and" not in filtered_tokens
    assert "sample" in filtered_tokens

if __name__ == '__main__':
    test_clean_tweet()
    test_lower_start_fct()
    test_lemma_fct()
    test_tokenize_tweet()
    test_remove_stopwords()
    print("All tests passed!")
