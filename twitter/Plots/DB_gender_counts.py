import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/wybek/PycharmProjects/Web/twitter/genderCounts/DBcounts.csv')

states = data['State']
males = data['Male']
females = data['Female']

ratio =  [int(b) / int(m) for b,m in zip(males, females)]

plt.figure(figsize=(8.0, 5.0))
plt.grid()
hst = plt.plot(states, ratio, color = 'r', linestyle='None', markersize = 7.0, marker='o')
plt.xticks(fontsize=8, rotation='vertical')
plt.xlabel('States')
plt.ylabel('Male to Female ratio')
plt.title('Male to Female ratio per state')
plt.savefig('c://users//wybek//PycharmProjects//Web//twitter//PlotFigures//MFratioDBmethod.png',  bbox_inches='tight')

plt.show()



