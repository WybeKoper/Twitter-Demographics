import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/wybek/PycharmProjects/Web/twitter/genderCounts/culturecounts.csv')
print(data)
data = data.drop([0, 1, 5, 6])
print(data)
culture = data['Culture'].tolist()
counts = data['0'].tolist()
total = sum(counts)
counts = [x / total for x in counts]

otherLabels =['Asian', 'Black', 'Hispanic', 'White']

plt.figure(figsize=(8.0, 5.0))
plt.grid()
hst = plt.plot(otherLabels, counts, color = 'r', linestyle='None', markersize = 7.0, marker='o')
plt.xticks(fontsize=8, rotation='vertical')
plt.xlabel('Ethnicity')
plt.ylabel('Number of Users Normalized')
plt.title('Ethnicity of Users Making Political Tweets')
plt.savefig('c://users//wybek//PycharmProjects//Web//twitter//PlotFigures//CultureOfUsers.png',  bbox_inches='tight')
plt.show()