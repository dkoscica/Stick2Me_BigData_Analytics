# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 23:37:43 2017

@author: Dominik
"""

"""
Print methods
"""
def show_header(text):
    print("\n")
    print("###############################################")
    print(text)
    print("###############################################")
    
def print_tweet(tweet):
    print("Date:", tweet.created_at)
    print("Name:", tweet.user.name)
    print("Screen name:", tweet.user.screen_name)
    print("Text:", tweet.text)
    print()
    
def print_user(user):
    print("Id:", user.id)
    print("Created at:", user.created_at)
    print("Name:", user.name)
    print("Screen name:", user.screen_name)
    print("Description:", user.description)
    print("Followers count:", user.followers_count)
    print("Friends count:", user.friends_count)
    print("Favorites count:", user.favourites_count)
    print("Statuses count:", user.statuses_count)
    print()
