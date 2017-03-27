# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 00:32:35 2017

@author: Dominik
"""

import nltk 
from nltk import FreqDist

from tweepy_wrapper import TweepyWrapper
from util import PrintHelper 

class NLTKWrapper:
    
    #Members
    __ignored_words = ["stick2me", "tvz_dkoscica"]
    __concordance_words = ["dobar", "odličan", "super", "loš", "neispravan"]
    
    def __init__(self):
        PrintHelper.print_header("NLTKWrapper created!\nIgnored words:" + str(self.__ignored_words))
        
    def tokenize(self, text):
        tokens = nltk.word_tokenize(text)
        return tokens
        
    def normalize(self, text):
        return text.lower()

    def lexical_diversity(self, text):
        if text:
            return len(text) / len(set(text))
        return 0
    
    def percentage(self, count, total):
        return 100 * count / total
    
    def collocations(self, text_list):
        nltkText = nltk.Text(text_list)
        return nltkText.collocations()
        
    def concordance(self, text_list, word):
        nltkText = nltk.Text(text_list)
        return nltkText.concordance(word)
        
    def draw_plot(self, tokens):
        nltkText = nltk.Text(tokens)
        fdist = FreqDist(nltkText)
        return fdist.plot(20)
        
    def tokenize_without_punctuation(self, text):
        tokens = self.tokenize(text)
        filteredTokens = []
        for token in tokens:
            if len(token) > 4 and token not in self.__ignored_words:
                filteredTokens.append(token)
        return sorted(filteredTokens, key=len)
        
    def analize_text(self, collection_name, text):
        #print("Text: " + text)
        
        #db.tweets.From_2016_12_23_To_2016_12_30
        formated_date = collection_name.strip("db.tweets.From_").replace("_To_", " - ").replace("_", ".")
        image_name = "nltk_" + collection_name.strip("db.tweets.From_") + ".png"
        #print(formated_date)
        #print(image_name)
        
        normalizedText = self.normalize(text)
        tokens = self.tokenize(normalizedText)
        tokens_without_punctuation = self.tokenize_without_punctuation(normalizedText)
        
        #print("\nTokens: ", tokens_without_punctuation)
        #print("Collocations:", self.collocations(normalizedText))
        #print("Lexical diversity:", self.lexical_diversity(normalizedText))
        
        print("<h3>Text mining " + formated_date + "</h3><br>")
        print("<b>Tokens: </b>", set(tokens_without_punctuation))
        print("<b>Collocations: </b>", self.collocations(normalizedText))
        print("<br><b>Lexical diversity: </b>", self.lexical_diversity(normalizedText))
        
        self.print_top_words_from_text(normalizedText) 
        
        print("<br>")
        print('<img src="Images/' + image_name + '">')

        for concordance_word in self.__concordance_words:
            self.print_concordance_result(tokens_without_punctuation, concordance_word)
    
        self.draw_plot(tokens_without_punctuation)
        
    """
    Print methods
    """
    
    """
    Console
    """
    def print_top_words_from_text(self, text):
        print("\nTop 10 words:")
        tokens = self.tokenize_without_punctuation(text)
        
        nltkText = nltk.Text(tokens)
        fdist = FreqDist(nltkText)
        
        for word, frequency in fdist.most_common(10):
            print("%s : %d" % (word, frequency))
        return

    def print_concordance_result(self, text_list, word):
        print("\nConcordance: " + word)
        self.concordance(text_list, word)
        
    """
    Html
    """
    def print_top_words_from_text(self, text):
        print("\n<b>Top 10 words</b>")
        tokens = self.tokenize_without_punctuation(text)
        
        nltkText = nltk.Text(tokens)
        fdist = FreqDist(nltkText)
        print("<ul>")
        for word, frequency in fdist.most_common(10):
            print("  <li>")
            print("     %s : <b>%d</b>" % (word, frequency))
            print("  </li>")
        print("</ul>")

    def print_concordance_result(self, text_list, word):
        print("Concordance: " + "<b>" + word + "</b>")
        print("<br>")
        self.concordance(text_list, word)
        print("<br><br>")
        
    
