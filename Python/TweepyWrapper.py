# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:34:41 2017

@author: Dominik
"""

import tweepy

class TweepyWrapper:
    
    #Constants
    CONSUMER_KEY = "GcCRUCVDeJf0H6zG7k3BqCsXV"
    CONSUMER_SECRET = "I6RvI3tFjnd5XL1BgfDNqqJ1bVSXinBYooTOGJpg7KCug9mlLt"
    ACCESS_TOKEN = "810627882104057856-nxELiESEiHYvZCbymNDI98us80A2Ayo"
    ACCESS_TOKEN_SECRET = "1uAWrovjiDQvztHfiG9K6C94MrIMs3GH1dncuJO5DXiAW"
    
    #Members
    __followers = []
    __mostInfluentialFollowers = []

    __allMyTweets = []
    __allTweetsFromMyFollowers = []
        
    def __init__(self):
        #OAuth
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN,  self.ACCESS_TOKEN_SECRET)
        
        #Construct the API instance
        self.api = tweepy.API(auth)
        
    """
    Print methods
    """
    def print_user_information(self):
        show_header("Get all the information about @TVZ_dkoscica")
        user = self.api.me()
        print_user(user)
        
    """
    Follower methods
    """
    def get_my_followers(self):
        if not self.__followers:
            self.__followers = self.api.followers()
            return self.__followers
        return self.__followers
    
    def get_most_influential_followers(self):
        if not self.__mostInfluentialFollowers:
            self.__mostInfluentialFollowers = sorted(self.get_my_followers(), 
                                                     key=lambda user: user.statuses_count, reverse = True)
            return self.__mostInfluentialFollowers
        return self.__mostInfluentialFollowers
        
    def print_all_my_followers(self):
        show_header("All my followers")
        for follower in self.get_my_followers():
            print_user(follower)
            
    def print_most_influential_followers(self):
        show_header("Top 10 most influential followers")
        for follower in self.get_most_influential_followers()[:10]:
            print_user(follower)  
     
    """
    Tweets methods
    """
    def get_all_my_tweets(self):
        if not self.__allMyTweets:
            self.__allMyTweets = tweepy.Cursor(self.api.user_timeline).items()
            return self.__allMyTweets
        return self.__allMyTweets
        
    def get_all_tweets_from_user(self, screen_name):
        return self.api.user_timeline(screen_name = screen_name, count=500) 
        
    def get_all_tweets_from_my_followers(self):
        if not self.__allTweetsFromMyFollowers:
            #allTweetsFromMyFollowers.append(allMyTweets)
            for follower in self.get_my_followers():
                allTweetsFromUser = self.get_all_tweets_from_user(follower.screen_name)
                self.__allTweetsFromMyFollowers.extend(allTweetsFromUser)
            return self.__allTweetsFromMyFollowers 
            
        return self.__allTweetsFromMyFollowers 
            
    def get_all_tweets_which_contain_Stick2Me(self):
        tweetsThatContainStick2Me = []
        for tweet in self.get_all_tweets_from_my_followers():
            if "Stick2Me" in tweet.text:
                tweetsThatContainStick2Me.append(tweet)
        return tweetsThatContainStick2Me

    def print_all_tweets_from_me(self):
        show_header("All tweets from @TVZ_dkoscica")
        for tweet in self.get_all_my_tweets():
            print_tweet(tweet)
            
    def print_retweets_of_me(self):
        retweets = self.api.retweets_of_me()
        numberOfRetweets = str(len(retweets))
        show_header("Retweets of me\nNumber of retweets: "  + numberOfRetweets)
        for tweet in retweets:
            print_tweet(tweet)
                           
    def print_all_tweets_which_contain_Stick2Me(self):
        #+ str(len(self.get_all_tweets_which_contain_Stick2Me_or_TVZ_dkoscica))
        show_header("Tweets that contain Stick2Me or @TVZ_dkoscica\nNumber of tweets: ")
        for tweet in self.get_all_tweets_which_contain_Stick2Me():
            print_tweet(tweet)