# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 23:13:50 2017

@author: Dominik
"""

def main():

    tweepyWrapper = TweepyWrapper()
    
    tweepyWrapper.print_user_information()
    
    #tweepyWrapper.print_all_my_followers()
    #tweepyWrapper.print_most_influential_followers()
    
    #tweepyWrapper.print_all_tweets_from_me()
    #tweepyWrapper.print_retweets_of_me()

    allTweetsWhichContainStick2MeOrTVZ_dkoscica = tweepyWrapper.get_all_tweets_which_contain_Stick2Me()
    show_header("Number of Tweets that contain Stick2Me: "  + str(len(allTweetsWhichContainStick2MeOrTVZ_dkoscica)))
    tweepyWrapper.print_all_tweets_which_contain_Stick2Me()

    pyMongoWrapper = PyMongoWrapper()
    pyMongoWrapper.insert_all_tweets(allTweetsWhichContainStick2MeOrTVZ_dkoscica)    
    pyMongoWrapper.print_one_tweet()
    #pyMongoWrapper.print_all_collection_tweets()
    
if __name__ == "__main__": main()