# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 23:13:50 2017

@author: Dominik
"""

import sys
sys.path.append('Python/') 

from util import PrintHelper 
from tweepy_wrapper import TweepyWrapper
from pymongo_wrapper import PyMongoWrapper
from nltk_wrapper import NLTKWrapper
from sna_wrapper import SNAWrapper

import plotly.plotly as py
import plotly.graph_objs as go

import nltk
from time import sleep

def main():

    tweepyWrapper = TweepyWrapper()
    
    tweepyWrapper.print_user_information()
    
    tweepyWrapper.print_all_my_followers()
    tweepyWrapper.print_most_influential_followers()
    
    tweepyWrapper.print_all_tweets_from_me()
    tweepyWrapper.print_retweets_of_me()
    
    allFollowerTweetsWhichContainStick2Me = tweepyWrapper.get_follower_tweets_which_contain_Stick2Me()
    tweepyWrapper.print_all_tweets_which_contain_Stick2Me()

    pyMongoWrapper = PyMongoWrapper()
    #pyMongoWrapper.insert_all_tweets(allFollowerTweetsWhichContainStick2Me)   
    pyMongoWrapper.print_all_collection_tweets()

    
    collectionNames = pyMongoWrapper.get_all_collection_names()
    
    """
    Basic data analytics
    """
    for collectionName in collectionNames:
        PrintHelper.print_header("Collection name: " + collectionName)
        pyMongoWrapper.print_collection(collectionName)

    """"
    NLTK
    """
    nltkWrapper = NLTKWrapper()
    
    #targetCollectionName = "tweets.From_2017_02_08_To_2017_02_15"
    for collectionName in collectionNames:
        PrintHelper.print_header("Collection name: " + collectionName)
        tweetTextSummaryFromCollection = pyMongoWrapper.get_tweet_text_summary_for_collection(collectionName)
        nltkWrapper.analize_text(collectionName, tweetTextSummaryFromCollection) 

    """
    SNA
    """
    targetCollectionName = "tweets.From_2017_02_08_To_2017_02_15"
    for collectionName in collectionNames:
        if collectionName in targetCollectionName:
            PrintHelper.print_header("Collection name: " + collectionName)
            vertexes = pyMongoWrapper.get_tweet_vertexes_for_collection(collectionName) 
            SNAWrapper(collectionName, vertexes).create_sna_analysis_html()
            #SNAWrapper(collectionName, vertexes).create_sna_analysis()
            break
           
if __name__ == "__main__": main()