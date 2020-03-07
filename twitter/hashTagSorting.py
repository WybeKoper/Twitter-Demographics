import pandas as pd

hashtags = pd.read_csv('c://users/wybek/PycharmProjects/web/twitter/hashTags/hashtagDF', names =['hashtag', 'count'])
print(hashtags)
result = hashtags.sort_values('count', ascending=False)
print(result)
result.to_csv('c://users/wybek/PycharmProjects/web/twitter/hashTags/hashtagDFsorted.csv')