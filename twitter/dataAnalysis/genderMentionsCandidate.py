import os
import pandas as pd

fileLoc = "c:/users/wybek/pycharmprojects/web/twitter/stateFilesAPIGender/"
fileNames = os.listdir(fileLoc)

data = pd.DataFrame()
for count, file in enumerate(fileNames):
    data = pd.concat([data, pd.read_csv(fileLoc + file, index_col=0)])

candidateLastnames = ['Sanders', 'Warren', 'Yang', 'Biden', 'Buttigieg', 'Steyer', 'Booker', 'Klobuchar', 'Bloomberg', 'Gabbard']
counts = {}
for name in candidateLastnames:
    counts[name + "_M"] = 0
    counts[name + "_F"] = 0


for index, row in data.iterrows():
    genderDB = str(row['genderDB'])
    genderAPI = str(row['GenderApi'])
    candidates = str(row['candidates']).split(" ")
    del candidates[-1]
    for candidate in candidates:
        if genderDB == 'M' and genderAPI != 'feminine':
            counts[candidate + "_M"] +=1
        if genderDB == 'F' and genderAPI != 'masculine':
            counts[candidate + "_F"] +=1

        if genderDB != 'F' and genderAPI == 'masculine':
            counts[candidate + "_M"] +=1
        if genderDB != 'M' and genderAPI == 'feminine':
            counts[candidate + "_F"] +=1

countsList = list(counts.values())
males = countsList[::2]
females = countsList[1::2]
ratios = [int(b) / int(m) for b,m in zip(males, females)]
output = pd.DataFrame({'Candidates': candidateLastnames, "MaleCount": males, 'FemaleCount': females, 'M/F': ratios})

output.to_csv('C:/Users/wybek/PycharmProjects/Web/twitter/genderCounts/genderPerCandidate.csv')
