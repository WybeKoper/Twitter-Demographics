import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('C:/Users/wybek/PycharmProjects/Web/twitter/genderCounts/ageCounts.csv')
data = data.drop([132])

bins=[]
for i in range(6):
    bins.append(0)

labels = ['< 18', '18 - 29', '30 - 44', '45 - 54', '55 - 64', '65+']

for index, row in data.iterrows():
    age = row['Age']
    count = row['0']
    age = int(age.split('.')[0])
    if age < 18:
        bins[0] += count
    if 18 <= age <= 29:
        bins[1] += count
    if 29 < age <= 44:
        bins[2] += count
    if 44 < age <= 54:
        bins[3] += count
    if 54 < age <= 64:
        bins[4] +=count
    if age > 64:
        bins[5] += count


totalUsers = sum(bins)
bins = [x / totalUsers for x in bins]

plt.figure(figsize=(8.0, 5.0))
plt.grid()
hst = plt.plot(labels, bins, color = 'r', linestyle='None', markersize = 7.0, marker='o')
plt.xticks(fontsize=10)
plt.xlabel('Age')
plt.ylabel('Number of Users Normalized')
plt.title('Age of Users making Political Tweets')
plt.savefig('c://users//wybek//PycharmProjects//Web//twitter//PlotFigures//AgeOfUsers.png',  bbox_inches='tight')
plt.show()

#mean and median calculation
ageList = data['Age']
countList = data['0']
multp = [int(b.split('.')[0]) * int(m) for b,m in zip(ageList, countList)]
print(sum(multp)/sum(countList))

