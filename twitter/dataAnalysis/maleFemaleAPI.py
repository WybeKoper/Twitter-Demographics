import os
import pandas as pd

fileLoc = "c:/users/wybek/pycharmprojects/web/twitter/stateFilesAPIGender/"
fileNames = os.listdir(fileLoc)

state = []
data = pd.DataFrame()
for count, file in enumerate(fileNames):
    stateName = file.split("_")[3].split('.')[0]
    state.append(stateName)
    data = pd.concat([data, pd.read_csv(fileLoc + file, index_col=0)])

data = data.drop(['Unnamed: 0.1'], axis = 1)
countsCulture = data.groupby(['Culture']).size().reset_index()
countsAge = data.groupby(['Age']).size().reset_index()
countsGender = data.groupby(['GenderApi']).size().reset_index()

countsCulture.to_csv('C:/users/wybek/PycharmProjects/web/twitter/genderCounts/culturecounts.csv')
countsAge.to_csv('C:/users/wybek/PycharmProjects/web/twitter/genderCounts/ageCounts.csv')
countsGender.to_csv('C:/users/wybek/PycharmProjects/web/twitter/genderCounts/countsGenderAPI.csv')


