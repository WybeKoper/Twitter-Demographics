import os
import pandas as pd

fileLoc = "c:/users/wybek/pycharmprojects/web/twitter/genderDBMethod/"
fileNames = os.listdir(fileLoc)

state = []
males =[]
females =[]
undetermined =[]
for count, file in enumerate(fileNames):
    stateName = file.split("_")[2].split('.')[0]
    state.append(stateName)
    data = pd.read_csv(fileLoc + file, index_col=0)
    counts = data.groupby(['genderDB']).size().tolist()
    # print(stateName)
    # print(counts)
    females.append(counts[0])
    males.append(counts[1])
    undetermined.append(counts[2])

m = sum(males)
w = sum(females)
u = sum(undetermined)
total = m + w + u
print(total)
print(m + w)
print((m+w)/total)
print(state)

combined = pd.DataFrame({'State': state, 'Male': males,'Female': females, 'Undetermined': undetermined})
print(combined)
combined.to_csv('C:/users/wybek/PycharmProjects/Web/twitter/genderCounts/DBcounts.csv')
print(m/w)
