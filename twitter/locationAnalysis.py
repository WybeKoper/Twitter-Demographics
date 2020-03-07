import json
import pandas as pd

namesGender = pd.read_csv('c://users//wybek//downloads//name_gender.csv')
names = namesGender['name']
namesList = names.tolist()
genders = namesGender['gender']

nameGenderDict = dict(zip(names,genders))

candidates = ['Bernie', 'Yang', 'Biden', 'Warren']

counts = {}
for item in candidates:
    counts[item + 'M'] = 0
    counts[item + 'F'] = 0

data = {}

individuals = {}
it = 0
with open('dataSEt.json') as file:
    for line in file:
        if (line != "\n"):
            tweet = json.loads(line)
            userid = tweet['user']['id']
            lang = tweet['lang']
            text = tweet['text']
            loc = tweet['user']['location']
            name = tweet['user']['name']
            screenname = tweet['user']['screen_name']
            photo = tweet['user']['profile_image_url']
            hashtags = tweet['entities']['hashtags']
            if lang == 'en':
                if loc is not None:
                    if "Iowa" in loc:
                        for candidate in candidates:
                             if candidate in text:
                                 if userid in individuals:
                                     individuals[userid] += 2
                                 else:
                                    individuals[userid] = 0
                                    counts[candidate + 'M'] += 1
                                    data[str(it)] = [str(userid) + "i", name, screenname, text, photo, loc]
                                    it+=1
#note accurate location filter


output = pd.DataFrame.from_dict(data, 'index')

#not accu
print(individuals)
print(counts)
#print(output)
output.to_csv('c://users//wybek//PycharmProjects//Web//twitter//cleansedTweets//IowaNoGender.csv')