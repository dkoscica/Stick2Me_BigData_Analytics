## To start the Jupyter Notebook simply click on:
[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/dkoscica/stick2me_bigdata_analytics)
## If the Jupyter Notebook won't open click on:
[Index.ipynb](https://github.com/dkoscica/Stick2Me_BigData_Analytics/blob/master/index.ipynb)

## MongoDB
Contains all MongoDB scripts.

#### mongodb_delete_script.js
This script is used to delete all MongoDB database data.

#### mongodb_operations.js
Contains various MongoDB operations such as totalNumberOfTweets, sortedUsersWithMostStick2MeTweets, tweetsPerUserByInterval, tweetsPerWeek etc.

#### mongodb_split_all_tweets_script.js
Used to split all collected tweets by a specific interval.

## Python
Contains all Python scripts.

#### util.py
Contains various print methods and a TweetDocument model used to map Tweepy tweet object to MongoDB document objects.

#### tweepy_wrapper.py
Contains authentications logic, methods to retrive followers, tweets and users.

#### pymongo_wrapper.py
Used to persist all collected tweet data which were retrieved from tweepy_wrapper.py. Contains mapping logic to map Tweepy tweet objects to MongoDB document objects.

#### nltk_wrapper.py
Wrapper class used for text mining via the nltk python library.

#### sna_wrapper.py
Wrapper class used for analysis via the sna python library.

#### main.py
Main class which is used to instantiate and manipulate with various wrapper classes.
