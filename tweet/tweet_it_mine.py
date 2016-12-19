#!/usr/bin/env python2
##https://blog.twitter.com/developer

import tweepy
#from subprocess import Popen, PIPE

class API_Handler(object):

  config = {
    "consumer_key"        : "tq2HJkZRwbRvKCvGi0OOAKtbB",
    "consumer_secret"     : "msoTcqHE1lFJLzciVQjv8PqgHm5OhkpHOdjtJf3XUp6DPXElP0",
    "access_token"        : "795372839755010048-wYROqmCLqk5WmK0UBzBZgAfkROGO7q5",
    "access_token_secret" : "DQz6rQY57H5e7FaO2f8YyuEbQlceOOhWwfjB38edWA0rL",
    }

  def __init__(self,config={}):
    if config:
      self.config = config
    else:
      self.config = API_Handler.config

  def get_api(self,cfg):
    self.auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    self.auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(self.auth)

  def tweet(self, tweet):
    # Fill in the values noted in previous step here

    self.api = self.get_api(self.config)

    self.tweet = tweet
  
    self.status = self.api.update_status(status=self.tweet)

if __name__ == "__main__":
  tweeter = API_Handler()
  tweeter.tweet('Test')