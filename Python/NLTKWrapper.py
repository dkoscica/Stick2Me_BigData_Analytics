# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 00:32:35 2017

@author: Dominik
"""

import nltk
from nltk.book import*

tweepyWrapper = TweepyWrapper()
allTweetsWhichContainStick2MeOrTVZ_dkoscica = tweepyWrapper.get_all_tweets_which_contain_Stick2Me()
#show_header("Number of Tweets that contain Stick2Me: "  + str(len(allTweetsWhichContainStick2MeOrTVZ_dkoscica)))
#tweepyWrapper.print_all_tweets_which_contain_Stick2Me()

tweet = allTweetsWhichContainStick2MeOrTVZ_dkoscica[0].text

#print(len(text3))
#print(sorted(set(text3)))

#print(len(text3)/len(set(text3)))

print(text3.count("smote"))
#print(tweet.concordance("#Stick2Me"))

def lexical_diversity(text):
    return len(text) / len(set(text))
    
def percentage(count, total):
    return 100 * count / total
"""    
print(lexical_diversity(text5))

print("Percentage: " + str(percentage(text4.count("a"), len(text4))))

distributionFreq = FreqDist(text1)
vocabular = list(distributionFreq.keys())

for key in vocabular[:10]:
    print(key)
    
for key in distributionFreq.most_common(10):
    print(key)
"""

vocabular = set(text1)
long_words = [w for w in vocabular if len(w) > 15]
              
#print(sorted(long_words))

#print(text4.collocations())

tweetDist = FreqDist(tweet)
rawText = type(tweet)

#Razbijanje stringova u rijeci i uklanjaje punkcije
tokens = nltk.word_tokenize(text4)