# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 23:37:43 2017

@author: Dominik
"""

from enum import Enum

class TweetDocument(Enum):
     created_at = "created_at"
     user_name = "user_name"
     text = "text"
     vertex1 = "screen_name"
     vertex2 = "in_reply_to_screen_name"
 
class PrintHelper(object):
    
    def print_header(text):
        print("")
        print("###############################################")
        print(text)
        print("###############################################")
    
    def print_footer():
        print("###############################################\n")
    
    def print_tweet(tweet):
        print("Date:", tweet.created_at)
        print("Name:", tweet.user.name)
        print("Text:", tweet.text)
        print("Vertex1:", tweet.user.screen_name)
        print("Vertex2:", tweet.in_reply_to_screen_name)
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

'''
"""
Used to print html formated information
"""
def print_tweet(tweet):
    print(" <li>")
    print("   <b>Date:</b>", tweet.created_at, "<br>")
    print("   <b>Name:</b>", tweet.user.name, "<br>")
    print("   <b>Screen name:</b>", tweet.user.screen_name, "<br>")
    print("   <b>Text:</b>", tweet.text, "<br>")
    print(" </li>")
    
def print_user(user):
    print(" <li>")
    print("   <b>Id:</b>", user.id, "<br>")
    print("   <b>Created at:</b>", user.created_at, "<br>")
    print("   <b>Name:</b>", user.name, "<br>")
    print("   <b>Screen name:</b>", user.screen_name, "<br>")
    print("   <b>Description:</b>", user.description, "<br>")
    print("   <b>Followers count:</b>", user.followers_count, "<br>")
    print("   <b>Friends count:</b>", user.friends_count, "<br>")
    print("   <b>Favorites count:</b>", user.favourites_count, "<br>")
    print("   <b>Statuses count:</b>", user.statuses_count, "<br>")
    print(" </li>")
'''    