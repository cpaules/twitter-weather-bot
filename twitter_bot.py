import tweepy
import time

from secret import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



# location - mention.user.location

def get_latest_tweet_id():
  my_id = api.me().id
  tweets = api.user_timeline(id = my_id, count = 1)
  last_seen_id = tweets[0].id
  return last_seen_id

def reply_to_tweets():
  last_seen_id = get_latest_tweet_id()
  mentions = api.mentions_timeline(last_seen_id)
  print('replying to tweets...')
  for mention in reversed(mentions):
    if '#weather' in mention.text.lower():
      print(str(mention.id) + ' - ' + mention.text.lower())
      api.update_status('@' + mention.user.screen_name + ' WIP: getting you the weather!', mention.id)

while True:
  reply_to_tweets()
  time.sleep(2)