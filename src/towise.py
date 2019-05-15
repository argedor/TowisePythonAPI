import requests
import constants
import re

class Towise:
    def __init__(self,app_id,app_key):
        self.headers = {
            "appid":app_id,
            "appkey":app_key,
            'accept': 'application/json'
        }
    def checkImage(self,image):
        res = {}
        if(re.match("(data:image)",image)):
            res['image_base64'] = image
        else:
            res['image_url'] = image
        
        return res
    
    def faceDetect(self,image):
        data = self.checkImage(image)
        res = requests.post(url = constants.BASE_URL + constants.detect['face'], headers=self.headers, data = data)
        return res.json()

    def bodyDetect(self,image):
        data = self.checkImage(image)
        res = requests.post(url = constants.BASE_URL + constants.detect['body'], headers=self.headers, data = data)
        return res.json()
    
    def emotionDetect(self,image):
        data = self.checkImage(image)
        res = requests.post(url = constants.BASE_URL + constants.detect['emotion'], headers=self.headers, data = data)
        return res.json()

    def faceComparing(self,image):
        data = self.checkImage(image)
        res = requests.post(url = constants.BASE_URL + constants.recognize['face'], headers=self.headers, data = data)
        return res.getjson()
    
    def getAllPerson(self):
        res = requests.get(url = constants.BASE_URL + constants.persons, headers=self.headers)
        return res.json()
    
    def getPerson(self,person_id):
        params = {"person_id":person_id}
        res = requests.get(url = constants.BASE_URL + constants.persons, headers=self.headers, params = params)
        return res.json()
    
    def addPerson(self,name):
        data = {"name":name}
        res = requests.post(url = constants.BASE_URL + constants.persons, headers=self.headers, data = data)
        return res.json()

    def removePerson(self,person_id):
        data = {"person_id":person_id}
        res = requests.delete(url = constants.BASE_URL + constants.persons, headers=self.headers, data = data)
        return res.json()
    
    def getAllFace(self,person_id):
        params = {"person_id":person_id}
        res = requests.get(url = constants.BASE_URL + constants.faces, headers=self.headers, params = params)
        return res.json()

    def getFace(self,face_id):
        params = {"face_id":face_id}
        res = requests.get(url = constants.BASE_URL + constants.faces, headers=self.headers, params = params)
        return res.json()
    
    
    def addFace(self,image,person_id,save):
        data = self.checkImage(image)
        data["person_id"] = person_id
        data["save_image"] = save
        res = requests.post(url = constants.BASE_URL + constants.faces, headers=self.headers, data = data)
        return res.json()
    
    def removeFace(self, face_id):
        data = {"face_id":face_id}
        res = requests.delete(url = constants.BASE_URL + constants.faces, headers=self.headers, data = data)
        return res.json()

if __name__ == "__main__":
    t = Towise("1","argedor123")
    image = ""
    print(t.faceDetect(image))