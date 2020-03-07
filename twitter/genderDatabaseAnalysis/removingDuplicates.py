import pandas as pd
import numpy as np
import os
candidateLastnames = ['Sanders', 'Warren', 'Yang', 'Biden', 'Buttigieg', 'Steyer', 'Booker', 'Klobuchar', 'Bloomberg', 'Gabbard']
columnNames = ['user_id', 'name', 'screen_name', 'text', 'pic', 'location','candidates','hashtags']

fileLoc = "c:/users/wybek/pycharmprojects/web/twitter/AllStatesTweets"
fileNames = os.listdir(fileLoc)
for file in fileNames:
    print(file)
    data = pd.read_csv("C:/Users/wybek/PycharmProjects/Web/twitter/AllStatesTweets/" + file, index_col=0, skiprows=1, names=['user_id', 'name', 'screen_name', 'text', 'pic', 'location','candidates','hashtags'])

    grouped = data.groupby(['user_id', 'name', 'screen_name', 'pic', 'location']).agg(lambda x: ''.join(set(x)))

    for index, row in grouped.iterrows():
        mentions = row['candidates']
        uniqueMentions = ""
        for name in candidateLastnames:
            if name in mentions:
                uniqueMentions += name + " "
        grouped['candidates'][index] = uniqueMentions

    grouped.to_csv("C:/Users/wybek/PycharmProjects/Web/twitter/stateFilesNoDuplicates/" + "no_Duplicates_" + file)