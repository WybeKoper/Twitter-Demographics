import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('c://users//wybek//PycharmProjects//Web//twitter//cleansedTweets//10CandidatesCounts.csv', names=['Candidate', 'Mentions'])
sorted = data.sort_values(by='Mentions',ascending=0)
candidates = sorted['Candidate']
counts = sorted['Mentions']


plt.figure()
hst = plt.plot(candidates, counts, color = 'r', linestyle='None', markersize = 8.0, marker='o')
plt.grid()
plt.xticks(fontsize=8, rotation='vertical')
plt.xlabel('Candidates')
plt.ylabel('Number of Mentions')
plt.title('Number of Mentions of Each Candidate on Twitter')
plt.savefig('c://users//wybek//PycharmProjects//Web//twitter//PlotFigures//MentionsNoFilter.png',  bbox_inches='tight')

plt.show()
