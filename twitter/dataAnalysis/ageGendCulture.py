import os
import pandas as pd

fileLoc = "c:/users/wybek/pycharmprojects/web/twitter/stateFilesAPIGender/"
fileNames = os.listdir(fileLoc)

data = pd.DataFrame()
for count, file in enumerate(fileNames):
    data = pd.concat([data, pd.read_csv(fileLoc + file, index_col=0)])

print(data)
countsCulture = data.groupby(['Culture']).size()
countsAge = data.groupby(['Age']).size().tolist()
countsGender = data.groupby(['GenderApi']).size()
print(countsCulture)
print(countsAge)
print(countsGender)

for i in range(len(countsAge)):
    print(countsAge[i])