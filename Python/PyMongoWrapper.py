# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:25:37 2017

@author: Dominik
"""

import pymongo
from pymongo import MongoClient
import pprint
import datetime

class PyMongoWrapper:
    
    #Never do this in production, 
    #the DB username an password must not be visible in code!!!
    DB_USERNAME = "admin"
    DB_PASSWORD = "stick2Me.Admin"
    
    HOST = "ds149069.mlab.com"
    PORT = str(49069)
    DATABASE_NAME = "stick2me_database"
    COLLECTION_NAME = "tweets.all"
    CONNECTION_URI = "mongodb://" + DB_USERNAME + ":" + DB_PASSWORD + "@" + HOST + ":" + PORT + "/" + DATABASE_NAME
 
    def __init__(self):
        self.client = MongoClient(self.CONNECTION_URI)
        self.database = self.client[self.DATABASE_NAME]
        self.collection = self.database[self.COLLECTION_NAME]
        self.print_collection(self.COLLECTION_NAME)
        print("Database connected!")
            
    """
    Insert all tweets into one MongoDB collection, 
    this collections will be later split by weeks via direct MongoDB commands
    """
    def insert_all_tweets(self, tweets):
        tweetDocuments = self.transform_tweets_to_tweet_documents(tweets)
        #tweetDocumentsSet = set(tweetDocuments) #Use set to remove possible duplicates
        self.collection.insert_many(tweetDocuments)
        print("insertAllTweets")
    
    def transform_tweets_to_tweet_documents(self, tweets):
        tweetDocuments = []
        for tweet in tweets:
            tweetDocuments.append(self.create_tweet_document(tweet))
        return tweetDocuments
    
    def create_tweet_document(self, tweet):
        return {"created_at": tweet.created_at,
                "name": tweet.user.name,
                "screen_name:": tweet.user.screen_name,
                "text:": tweet.text
                }
    
    """
    Print methods
    """
    def print_collection(self, collection_name):
        show_header("Collections")
        pprint.pprint(self.collection)

    def print_one_tweet(self):
        show_header("Find one Tweet")
        user = self.collection.find_one()
        pprint.pprint(user)

    def print_all_collection_tweets(self):
        show_header("All collection Tweets")
        for item in self.collection.find():
            pprint.pprint(item)
