# For this solution i had to get use of snscrape module and pandas module these are the terminal commands to install them.
# pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
# pip3 install pandas

import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list2 = [] # Creating a list to put tweet infos on it.

max_tweets = 500 # A max variable to stop looking for tweets.

# Using TwitterSearchScraper function to grab the tweet data and append the needed information to the created list.
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('request for startups since:2021-05-01 until:2021-05-03').get_items()):
    if i>max_tweets:
        break
    tweets_list2.append([tweet.content, tweet.user.username, tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.date])
    
# Creating a pandas DataFrame for ease of manipulation.
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Text', 'Username', 'like Count', 'retweet Count', 'reply Count', 'Datetime'])

# Sorting by likes,retweet,replies(discussions) and date.
tweets_df2.sort_values(['like Count','retweet Count','reply Count','Datetime'], ascending=[False,False,False,False],inplace=True)

# Saving to csv file.
tweets_df2.to_csv('text-query-tweets.csv', sep=',', index=False)