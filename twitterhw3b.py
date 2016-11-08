# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
import nltk
from textblob import TextBlob

# Unique code from Twitter
access_token = "443481916-E9R9G02yl4jtIZWFBO82t53Ga4Og7BE1OiHO7JL0"
access_token_secret = "kkamhblBbwjD9U98fe5fKB7uwlEf47VfeAQeC5t3Mf8BR"
consumer_key = "VW8tkb9etCH9Ud1qoEcpVVFH9"
consumer_secret = "dp9tyEswI5mBzcqfgv2i9BSkP6OkKmZe0brhCOkruIFM7sxELM"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('San Francisco')

total_pol = 0
total_sub = 0
num_tweets = 0

for tweet in public_tweets:
	num_tweets += 1
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	p = analysis.sentiment.polarity
	total_pol += p
	s = analysis.sentiment.subjectivity
	total_sub += s

avg_pol = total_pol / num_tweets
avg_sub = total_sub / num_tweets

#print (num_tweets)
#print (avg_pol)
#print (avg_sub)


print("Average subjectivity is " + str(avg_sub))
print("Average polarity is " + str(avg_pol))
