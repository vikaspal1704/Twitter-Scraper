import snscrape.modules.twitter as sntwitter
import csv
import pandas as pd

# Created a list to append all tweet attributes(data)
attributes_container = []


# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:john').get_items()):
    if i>100:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
print(tweets_df.head(30))
f = open(r"C:\Users\palv4\Desktop\CultureX\tw\data.txt",'w')
#data.savetxt(r'C:\Users\palv4\Desktop\CultureX\tw\data.txt', tweets_df.values, fmt='%d')
tweets_df.to_csv(r'C:\Users\palv4\Desktop\CultureX\tw\data.txt', header=None, index=None, sep=' ', mode='a')
f.close()