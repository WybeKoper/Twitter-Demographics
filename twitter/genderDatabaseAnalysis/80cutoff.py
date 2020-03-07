import pandas as pd

nameGender = pd.read_csv('C:/Users/wybek/PycharmProjects/Web/twitter/other/name_gender.csv')
nameGenderThreshold = nameGender[nameGender.probability >= 0.8]

print(nameGender)
print(nameGenderThreshold)

nameGenderThreshold.to_csv('C:/Users/wybek/PycharmProjects/Web/twitter/other/name_gender_Thresholded.csv')