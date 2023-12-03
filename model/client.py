import requests
import json


class Client:
    def __init__(self, host, api):
        self.api = api
        self.host = host
    
    def getServices(self, endpoint):
        response = requests.get(self.host + self.api + endpoint)
        response_dict = json.loads(response.text)
        return response_dict
    

    def createServices(self, payload, endpoint):
        response = requests.post(self.host + self.api + endpoint, json=payload)
        response_dict = json.loads(response.text)
        return response_dict


    def getService(self, id_account, endpoint):
        response = requests.get(self.host + self.api + endpoint + '/?id_account=' + str(id_account))
        response_dict = json.loads(response.text)
        return response_dict

    def printJson(self, data):
        print(json.dumps(data, indent=1))


    def signIn(self, payload, endpoint):
        response = requests.post(self.host + self.api + endpoint, json=payload)
        if(response.status_code == 401):
            return None
        
        response_dict = json.loads(response.text)
        return response_dict
