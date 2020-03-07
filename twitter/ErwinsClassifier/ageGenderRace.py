from clarifai.rest import ClarifaiApp

# Instantiate a new Clarifai app by passing in your API key.
app = ClarifaiApp(api_key='')

import pprint

# Choose one of the public models.
#model = app.public_models.general_model



# Predict the contents of an image by passing in a URL.
#response = model.predict_by_url(url='https://scontent-amt2-1.xx.fbcdn.net/v/t31.0-8/14066423_164885937275109_636065762843700855_o.jpg?_nc_cat=100&_nc_oc=AQkIZw4L7XnJ8KlqYzYF19h1EP6V1i8nHVRgFsuifqx0iKLwsYGCLVTGNW9lz3yQAE8&_nc_ht=scontent-amt2-1.xx&oh=6def9007a7b3a46792316cb27f3c873c&oe=5E6C0ED5')

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

a = Demography()
a.get_demographics_data('http://pbs.twimg.com/profile_images/806805533705453568/9pjur5OB.jpg')


print(a.get_age())
print(a.get_multicultural())
print(a.get_gender())
