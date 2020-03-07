import os
import pandas as pd

fileLoc = "c:/users/wybek/pycharmprojects/web/twitter/stateFilesAPIGender/"
fileNames = os.listdir(fileLoc)

data = pd.DataFrame()
for count, file in enumerate(fileNames):
    data = pd.concat([data, pd.read_csv(fileLoc + file, index_col=0)])

total = 0
classified = 0
dif = 0
same = 0
advantageAPI = 0
advantageDB = 0
for index, row in data.iterrows():
    total +=1
    genderDB = str(row['genderDB'])
    genderAPI = str(row['GenderApi'])
    if genderAPI != 'nan' or genderDB != 'U':
        classified +=1
    if genderAPI == 'masculine' and genderDB == 'F':
        dif +=1
    if genderAPI == 'feminine' and genderDB == 'M':
        dif += 1
    if genderAPI == 'feminine' and genderDB == 'F':
        same += 1
    if genderAPI == 'masculine' and genderDB == 'M':
        same += 1
    if genderAPI != 'nan' and genderDB == 'U':
        advantageAPI += 1
    if genderAPI == 'nan' and genderDB != 'U':
        advantageDB += 1

print(classified/total)
print(dif)
print((classified - dif)/total)
print(same/total)
print(advantageDB/total)
print(advantageAPI/total)

