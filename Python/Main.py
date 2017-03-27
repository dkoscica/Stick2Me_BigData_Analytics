# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 23:13:50 2017

@author: Dominik
"""

from util import PrintHelper 
from tweepy_wrapper import TweepyWrapper
from pymongo_wrapper import PyMongoWrapper
from nltk_wrapper import NLTKWrapper
from sna_wrapper import SNAWrapper

import plotly.plotly as py
import plotly.graph_objs as go

import nltk

def main():

    tweepyWrapper = TweepyWrapper()
    
    tweepyWrapper.print_user_information()
    
    tweepyWrapper.print_all_my_followers()
    tweepyWrapper.print_most_influential_followers()
    
    tweepyWrapper.print_all_tweets_from_me()
    tweepyWrapper.print_retweets_of_me()
   
    #allFollowerTweetsWhichContainStick2Me = tweepyWrapper.get_follower_tweets_which_contain_Stick2Me()
    #tweepyWrapper.print_all_tweets_which_contain_Stick2Me()

    pyMongoWrapper = PyMongoWrapper()
    #pyMongoWrapper.insert_all_tweets(allFollowerTweetsWhichContainStick2Me)   
    #pyMongoWrapper.print_all_collection_tweets()
    
    """
    Basic data analytics
    """
    #pyMongoWrapper.print_collection("tweets.From_2016_12_23_To_2016_12_30")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_01_To_2017_01_08")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_08_To_2017_01_15")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_15_To_2017_01_22")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_22_To_2017_01_29")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_29_To_2017_01_31")
    #pyMongoWrapper.print_collection("tweets.From_2017_02_01_To_2017_02_08")
    #pyMongoWrapper.print_collection("tweets.From_2017_02_08_To_2017_02_15")

    """"
    NLTK
    
    nltkWrapper = NLTKWrapper()
    
    collectionNames = pyMongoWrapper.get_all_collection_names()
    for collectioName in collectionNames:
        PrintHelper.print_header("Collection name: " + collectioName)
        tweetTextSummaryFromCollection = pyMongoWrapper.get_tweet_text_summary_for_collection(collectioName)
        nltkWrapper.analize_text(tweetTextSummaryFromCollection) 
        """
            
    #TODO replace with database vertex data
    vertexes = pyMongoWrapper.get_tweet_vertexes_for_collection("tweets.From_2017_01_01_To_2017_01_08")     
            
    graph = SNAWrapper(vertexes)
    graph.print_basic_graph_info()
    graph.print_additional_info()
    graph.draw_graph()
    
           
if __name__ == "__main__": main()