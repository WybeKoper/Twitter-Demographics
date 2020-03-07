import json
import pandas as pd


hashtagCounts = {}
with open('dataSEt.json') as file:
    for line in file:
        if (line != "\n"):
            tweet = json.loads(line)
            hashtags = tweet['entities']['hashtags']
            #print(hashtags)
            for tag in hashtags:
                if hashtagCounts.__contains__(tag['text']):
                    hashtagCounts[tag['text']] += 1
                else:
                    hashtagCounts[tag['text']] = 0

print(hashtagCounts)

dataFrame = pd.DataFrame.from_dict(hashtagCounts, 'index')
dataFrame.to_csv('c://users/wybek/PycharmProjects/web/twitter/hashTags/hashtagDF')