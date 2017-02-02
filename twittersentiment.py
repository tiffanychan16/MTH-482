import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'ItloBYUORZW9eMkf2tE9D5f6Y'
consumer_secret= '8B9QNNeDjZSLJhCD0o3JWw9IMcmJAEXmfYHayyTvxVggrfUjSw'

access_token='396855489-xvIu9Et1wYSOdskL8c9UIth2Dz28mb11Dbbi0YoW'
access_token_secret='woBWStYWo36ASgr5yzecieSV2LcvbPRLMesg5aNJX03pt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('NBA')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")