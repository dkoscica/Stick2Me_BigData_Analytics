# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:25:37 2017

@author: Dominik
"""

from util import *
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

        PrintHelper.print_header("Database connected!")
        self.print_collection_names()
        PrintHelper.print_footer()
            
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
        return {TweetDocument.created_at.name : tweet.created_at,
                TweetDocument.user_name.name : tweet.user.name,
                TweetDocument.text.name : tweet.text,
                TweetDocument.vertex1.name : tweet.user.screen_name,
                TweetDocument.vertex2.name : tweet.in_reply_to_screen_name
                }
                
    def get_collection_by_name(self, collection_name):  
        return self.database[collection_name]

    def get_all_collection_names(self):
        return self.database.collection_names(include_system_collections=False)

    """
    Tweet text methods
    """
    def get_tweet_text_summary_for_collection(self, collection_name):
        collection = self.get_collection_by_name(collection_name)
        tweetTextSummary = ""
        for tweet in collection.find():
            tweetTextSummary += tweet[TweetDocument.text.value]
        return tweetTextSummary
        
    """
    Vertex methods
    """
    def get_tweet_vertexes_for_collection(self, collection_name):
        collection = self.get_collection_by_name(collection_name)
        return list(collection.find({}, {"_id": 0, "vertex1": 1, "vertex2": 1}))
                
    """
    Print methods
    """
    def print_collection_names(self):
        PrintHelper.print_header("Collection names:")
        collection_names = self.database.collection_names(include_system_collections=False)
        for name in collection_names:
            print(name)
        
    def print_collection(self, collection_name):
        PrintHelper.print_header("Collection name:" + collection_name)
        collection = self.get_collection_by_name(collection_name)
        print("<ul>")
        for item in collection.find():
            #self.print_one_tweet(item)
            self.print_tweet_in_html_format(item)
        print("</ul>")

    def print_all_collection_tweets(self):
        PrintHelper.print_header("All collection Tweets")
        for tweet in self.collection.find():
            self.print_tweet(tweet)
            #pprint.pprint(item)
            
    def print_tweet(self, tweet):
        print("Date:", tweet[TweetDocument.created_at.name])
        print("Name:", tweet[TweetDocument.user_name.name])
        print("Text:", tweet[TweetDocument.text.name])
        print("Vertex1:", tweet[TweetDocument.vertex1.name])
        print("Vertex2:", tweet[TweetDocument.vertex2.name])
        print()   
        
    def print_tweet_in_html_format(self, tweet):
        print("  <li>")
        print("    <b>Date:</b>", tweet[TweetDocument.created_at.name], "<br>")
        print("    <b>Name:</b>", tweet[TweetDocument.user_name.name], "<br>")
        print("    <b>Text:</b>", tweet[TweetDocument.text.name], "<br>")
        print("    <b>Vertex1:</b>", tweet[TweetDocument.vertex1.name], "<br>")
        print("    <b>Vertext2:</b>", tweet[TweetDocument.vertex2.name], "<br>")
        print("  </li>")
        print("  <br>")