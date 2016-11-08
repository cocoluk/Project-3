# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy
import nltk

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

photo_path = '///Users/courtneyluk/Desktop/test.jpg'
hashtags = "#UMSI-206" + " #Proj3"
api.update_with_media(photo_path, status=hashtags)


#r = api.update_status('statuses/update_with_media',{'status':'#UMSI-206'+'Proj3'}, {'media[]':tweet})

#api.update_with_media(status = '#UMSI-206'+'#Proj3', media = fname)

#tweet = input('Enter image file name')
#status = api.update_status(status=tweet)

#filename = open(input('Enter image file name:'),'r')



print("""Tweet Posted, Check Twitter!""")