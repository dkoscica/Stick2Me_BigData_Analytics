# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:25:37 2017

@author: Dominik
"""

from Util import PrintHelper 
import pymongo
from pymongo import MongoClient
import pprint
import datetime
from enum import Enum

class TweetDocument(Enum):
     created_at = "created_at"
     user_name = "user_name"
     screen_name = "screen_name"
     text = "text"

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

        PrintHelper.show_header("Database connected!")
        self.print_collection_names()
            
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
        return {TweetDocument.created_at.value : tweet.created_at,
                TweetDocument.user_name.value : tweet.user.name,
                TweetDocument.screen_name.value : tweet.user.screen_name,
                TweetDocument.text.value : tweet.text
                }
                
    def get_collection_by_name(self, collection_name):  
        return self.database[collection_name]
                
    """
    Print methods
    """
    def print_collection_names(self):
        PrintHelper.show_header("Collection names:")
        collection_names = self.database.collection_names(include_system_collections=False)
        for name in collection_names:
            print(name)
        
    def print_collection(self, collection_name):
        PrintHelper.show_header("Collection name:" + collection_name)
        collection = self.get_collection_by_name(collection_name)
        print("<ul>")
        for item in collection.find():
            #self.print_one_tweet(item)
            self.print_one_tweet_in_html_format(item)
        print("</ul>")

    def print_one_tweet(self, tweet):
        print("Date:", tweet[TweetDocument.created_at.value])
        print("Name:", tweet[TweetDocument.user_name.value])
        print("Screen name:", tweet[TweetDocument.screen_name.value])
        print("Text:", tweet[TweetDocument.text.value])
        print()
        
    def print_one_tweet_in_html_format(self, tweet):
        print("  <li>")
        print("    <b>Date:</b>", tweet[TweetDocument.created_at.value], "<br>")
        print("    <b>Name:</b>", tweet[TweetDocument.user_name.value], "<br>")
        print("    <b>Screen name:</b>", tweet[TweetDocument.screen_name.value], "<br>")
        print("    <b>Text:</b>", tweet[TweetDocument.text.value], "<br>")
        print("  </li>")
        print("  <br>")

    def print_all_collection_tweets(self):
        PrintHelper.show_header("All collection Tweets")
        for item in self.collection.find():
            print_tweet(item)
            #pprint.pprint(item)
