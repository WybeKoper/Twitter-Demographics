import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

data = pd.read_csv('C:/Users/wybek/PycharmProjects/Web/twitter/genderCounts/genderPerCandidate.csv')
data = data.sort_values(by='MaleCount', ascending=False)
print(data)
names = data['Candidates']
maleCount = data['MaleCount']
femaleCount = data['FemaleCount']
ratios = data['M/F']


f = plt.figure(1)
plt.figure(figsize=(8.0, 5.0))
red_patch = mpatches.Patch(color='red', label='Female')
blue_patch = mpatches.Patch(color='blue', label='Male')

plt.legend(handles=[red_patch, blue_patch])
plt.grid()
hst = plt.plot(names, maleCount, color = 'b', linestyle='None', markersize = 7.0, marker='o')
hst = plt.plot(names, femaleCount, color = 'r', linestyle='None', markersize = 7.0, marker='o')

plt.xticks(fontsize=8, rotation='vertical')
plt.xlabel('Candidates')
plt.ylabel('Number of Male and Female Users')
plt.title('Male and Female users per Candidate')
plt.savefig('c://users//wybek//PycharmProjects//Web//twitter//PlotFigures//gender_Per_Candidate.png',  bbox_inches='tight')

f.show()


g = plt.figure(2)
plt.figure(figsize=(8.0, 5.0))
plt.grid()
hst = plt.plot(names, ratios, color = 'b', linestyle='None', markersize = 7.0, marker='o')

plt.xticks(fontsize=8, rotation='vertical')
plt.xlabel('Candidates')
plt.ylabel('Male to Female ratio')
plt.title('Male to Female ratio per Candidate')
plt.savefig('c://users//wybek//PycharmProjects//Web//twitter//PlotFigures//ratio_Per_Candidate.png',  bbox_inches='tight')
g.show()