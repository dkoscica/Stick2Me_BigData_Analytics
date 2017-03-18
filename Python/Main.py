# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 23:13:50 2017

@author: Dominik
"""

from TweepyWrapper import TweepyWrapper
from PyMongoWrapper import PyMongoWrapper

import plotly.plotly as py
import plotly.graph_objs as go

def main():

    tweepyWrapper = TweepyWrapper()
    
    #tweepyWrapper.print_user_information()
    
    #tweepyWrapper.print_all_my_followers()
    #tweepyWrapper.print_most_influential_followers()
    
    #tweepyWrapper.print_all_tweets_from_me()
    #tweepyWrapper.print_retweets_of_me()

    
    #allFollowerTweetsWhichContainStick2Me = tweepyWrapper.get_follower_tweets_which_contain_Stick2Me()
    #tweepyWrapper.print_all_tweets_which_contain_Stick2Me()

    pyMongoWrapper = PyMongoWrapper()
    #pyMongoWrapper.insert_all_tweets(allFollowerTweetsWhichContainStick2Me)   
    #pyMongoWrapper.print_all_collection_tweets()
    
    #pyMongoWrapper.print_collection("tweets.From_2016_12_23_To_2016_12_30")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_01_To_2017_01_08")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_08_To_2017_01_15")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_15_To_2017_01_22")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_22_To_2017_01_29")
    #pyMongoWrapper.print_collection("tweets.From_2017_01_29_To_2017_01_31")
    #pyMongoWrapper.print_collection("tweets.From_2017_02_01_To_2017_02_08")
    #pyMongoWrapper.print_collection("tweets.From_2017_02_08_To_2017_02_15")




    


    
    '''
    collection = pyMongoWrapper.get_collection_by_name("tweets.From_2017_01_01_To_2017_01_08")
    
                x=['23.12.2016-31.12.2016', '01.01.2017-01.08.2017', '13.01.2017', '20.01.2017', '27.01.2017', '03.02.2017', '10.02.2017', '17.02.2017'],

    
    
    print("Size"+ str(collection.count()))
    data = [go.Bar(
            x=['23.12.2016-31.12.2016', 
               '01.01.2017-08.01.2017',
               '08.01.2017-15.01.2017',
               '15.01.2017-22.01.2017',
               '22.01.2017-31.01.2017',
               '01.02.2017-08.02.2017',
               '08.02.2017-15.02.2017'
               '15.02.2017-22.02.2017'],
            y=[2, 7, 12, 14, 9, 16, 2, 0]
    )]

py.iplot(data, filename='basic-bar')
'''
       
if __name__ == "__main__": main()