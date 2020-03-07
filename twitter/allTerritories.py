import json
import pandas as pd




candidates = ['Bernie', 'Sanders', 'Elizabeth', 'Warren', 'Andrew','Yang', 'Joe', 'Biden', 'Pete','Buttigieg', 'Tom','Steyer' ,'Cory', 'Booker', 'Amy', 'Klobuchar', 'Mike', 'Bloomberg', 'Tulsi','Gabbard']
candidateLastnames = ['Sanders', 'Warren', 'Yang', 'Biden', 'Buttigieg', 'Steyer', 'Booker', 'Klobuchar', 'Bloomberg', 'Gabbard']


locations = pd.read_csv('C:/Users/wybek/PycharmProjects/Web/twitter/other/List-of-US-states-csv.csv', names=["States"])

locationsList = locations['States'].tolist()

for state in locationsList:
    print(state)
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
                        if loc is not None:
                            if state in loc:
                                mentioned = ""
                                for i in range(0, 20, 2):
                                    if candidates[i] in text or candidates[i+1] in text:
                                        counts[candidateLastnames[int(i/2)]] += 1
                                        mentioned += candidates[i+1] + " "
                                if mentioned is not "":
                                    data[str(it)] = [str(userid) + "i", name, screenname, text, photo, loc, mentioned, hashtags]
                                    it += 1
                except BaseException as e:
                    pass

    output = pd.DataFrame.from_dict(data, 'index')
    #countsAsDF = pd.DataFrame.from_dict(counts, 'index')
    #countsAsDF.to_csv('c://users//wybek//PycharmProjects//Web//twitter//cleansedTweets//10CandidatesCounts.csv')
    output.to_csv('c://users//wybek//PycharmProjects//Web//twitter//AllStatesTweets//' + state + '.csv')
