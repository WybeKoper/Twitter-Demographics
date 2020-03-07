import json
import pandas as pd
import matplotlib.pyplot as plt

namesGender = pd.read_csv('c://users//wybek//downloads//name_gender.csv')
names = namesGender['name']
namesList = names.tolist()
genders = namesGender['gender']

nameGenderDict = dict(zip(names,genders))

candidates = ['Bernie', 'Sanders', 'Elizabeth', 'Warren', 'Andrew','Yang', 'Joe', 'Biden', 'Pete','Buttigieg', 'Tom','Steyer' ,'Cory', 'Booker', 'Amy', 'Klobuchar', 'Mike', 'Bloomberg', 'Tulsi','Gabbard']
candidateLastnames = ['Sanders', 'Warren', 'Yang', 'Biden', 'Buttigieg', 'Steyer', 'Booker', 'Klobuchar', 'Bloomberg', 'Gabbard']
counts = {}
for item in candidateLastnames:
    counts[item] = 0

data = {}


it = 0
lel = 0
with open('10CandidatesFullName2.json') as file:
    for line in file:
        if (line != "\n"):
            try:
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
            #if loc is not None:
                #if "Iowa" in loc:
                    for i in range(0, 20, 2):
                        if candidates[i] in text or candidates[i+1] in text:
                            counts[candidateLastnames[int(i/2)]] += 1
                            data[str(it)] = [str(userid) + "i", name, screenname, text, photo, loc, candidates[i], hashtags]
                            it += 1
                    # for candidate in candidates:
                    #     if candidate in text:
                    #         counts[candidate] += 1
                    #         data[str(it)] = [str(userid) + "i", name, screenname, text, photo, loc, candidate]
                    #         it += 1
            except BaseException as e:
                pass

output = pd.DataFrame.from_dict(data, 'index')


countsAsDF = pd.DataFrame.from_dict(counts, 'index')

print(countsAsDF)
#print(output)
countsAsDF.to_csv('c://users//wybek//PycharmProjects//Web//twitter//cleansedTweets//10CandidatesCounts.csv')
#output.to_csv('c://users//wybek//PycharmProjects//Web//twitter//cleansedTweets//10Iowa.csv')
