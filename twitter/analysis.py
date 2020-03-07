import json
import pandas as pd

namesGender = pd.read_csv('c://users//wybek//downloads//name_gender.csv')
names = namesGender['name']
namesList = names.tolist()
genders = namesGender['gender']

nameGenderDict = dict(zip(names,genders))

candidates = ['Bernie', 'Warren', 'Yang', 'Biden', 'Sanders', 'Buttigieg', 'Steyer', 'Booker', 'Klobuchar', 'Bloomberg','Gabbard']

counts = {}
for item in candidates:
    counts[item + 'M'] = 0
    counts[item + 'F'] = 0

data = {}


it = 0
with open('dataSEt.json') as file:
    for line in file:
        if (line != "\n"):
            tweet = json.loads(line)
            lang = tweet['lang']
            text = tweet['text']
            loc = tweet['user']['location']
            name = tweet['user']['name']
            photo = tweet['user']['profile_image_url']
            hashtags = tweet['entities']['hashtags']
            if lang == 'en':
                if loc is not None:
                    firstName = tweet['user']['name'].split(' ', 1)[0]
                    print(loc)
                    if firstName in namesList:
                        it +=1
                        for candidate in candidates:
                            if candidate in text:
                                if nameGenderDict[firstName] is 'M':
                                    counts[candidate + 'M'] +=1
                                    data[str(it)] = [name, text, 'M', photo]
                                else:
                                    counts[candidate + 'F'] +=1
                                    data[str(it)] = [name, text, 'F', photo]

output = pd.DataFrame.from_dict(data, 'index')


print(counts)
print(output)
#output.to_csv('c://users//wybek//PycharmProjects//Web//twitter//cleansedTweets//gender.csv')