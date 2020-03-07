import pandas as pd
import re
import os
import urllib
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='14e655e63bc140eda9028ebd0a0ccfad')

class Demography:
    def __init__(self):
        self.response = None

    def get_general_data(self, url):
        model = app.public_models.general_model
        self.response = model.predict_by_url(url=url)
        if self.response['outputs'][0]['data']:
            return True
        else:
            print("No General Data")
            return False

    def get_demographics_data(self, url):
        model = app.models.get('demographics')
        self.response = model.predict_by_url(url=url)
        if self.response['outputs'][0]['data']:
            return True
        else:
            print("No Demographics Data")
            return False

    def is_human(self):
        for concept in self.response['outputs'][0]['data']['concepts']:
            if concept['value'] > 0.9:
                if "illustration" in concept['name'] or "fantasy" in concept['name'] or "halloween" in concept['name']:
                    print("Not Human")
                    return False
        for concept in self.response['outputs'][0]['data']['concepts']:
            if concept['value'] > 0.95:
                if "man" in concept['name'] or "woman" in concept['name'] or "girl" in concept['name'] or "boy" in concept['name']:
                        return True
        print("Not Human")
        return False


    def get_age(self):
        predict_value = 0
        predict_age = None

        for concept in self.response['outputs'][0]['data']['regions'][0]['data']['face']['age_appearance']['concepts']:
            if concept['value'] > predict_value:
                predict_value = concept['value']
                predict_age = concept['name']

        return predict_age

    def get_gender(self):
        predict_value = 0
        predict_gender = None

        for concept in self.response['outputs'][0]['data']['regions'][0]['data']['face']['gender_appearance'][
            'concepts']:
            if concept['value'] > predict_value:
                predict_value = concept['value']
                predict_gender = concept['name']

        return predict_gender

    def get_multicultural(self):
        predict_value = 0
        predict_appearance = None

        for concept in self.response['outputs'][0]['data']['regions'][0]['data']['face']['multicultural_appearance']['concepts']:
            if concept['value'] > predict_value:
                predict_value = concept['value']
                if "latino" in concept['name']:
                    predict_appearance = "latino or spanish origin"
                else:
                    predict_appearance = concept['name']

        return predict_appearance

# fileLoc = "c:/users/wybek/pycharmprojects/web/twitter/genderDBMethod"
# fileNames = os.listdir(fileLoc)
# for file in fileNames:
#     print(file)
#     data = pd.read_csv("C:/Users/wybek/PycharmProjects/Web/twitter/stateFilesNoDuplicates/" + file)
data = pd.read_csv("C:/Users/wybek/PycharmProjects/Web/twitter/genderDBMethod/GenderDBno_Duplicates_Florida.csv")
data['GenderApi'] = ""
data['Age'] = ""
data['Culture'] = ""

classifier = Demography()
it = 0
for index, row in data.iterrows():
    print(it)
    url = row['pic']
    stringURL = str(url)
    strList = stringURL.split('_normal')
    comb = strList[0] + strList[1]
    it += 1
    try:
        classifier.get_demographics_data(comb)
        data['GenderApi'][index] = str(classifier.get_gender())
        data['Age'][index] = str(classifier.get_age())
        data['Culture'][index] = str(classifier.get_multicultural())

    except Exception as e: pass

data.to_csv("C:/Users/wybek/PycharmProjects/Web/twitter/stateFilesApiGender/" + "API_"+ "GenderDBno_Duplicates_Florida.csv")
