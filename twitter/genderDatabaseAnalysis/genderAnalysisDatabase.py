import pandas as pd
import re
import os

namesGender = pd.read_csv('C:/Users/wybek/PycharmProjects/Web/twitter/other/name_gender_Thresholded.csv')
names = namesGender['name']
namesList = names.tolist()
genders = namesGender['gender']
nameGenderDict = dict(zip(names,genders))

fileLoc = "c:/users/wybek/pycharmprojects/web/twitter/stateFilesNoDuplicates"
fileNames = os.listdir(fileLoc)
for file in fileNames:
    print(file)
    data = pd.read_csv("C:/Users/wybek/PycharmProjects/Web/twitter/stateFilesNoDuplicates/" + file)
    data['genderDB'] = ""
    for index, row in data.iterrows():
        name = row['name']
        cropped = re.sub(r"([A-Z])", r" \1", name).split()
        firstName = cropped[0].title()
        if firstName in namesList:
            data['genderDB'][index] = str(nameGenderDict[firstName])
        else:
            data['genderDB'][index] = "U"

    data.to_csv("C:/Users/wybek/PycharmProjects/Web/twitter/genderDBMethod/" + "GenderDB" + file)
