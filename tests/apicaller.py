import requests
import json
import os
from dotenv import load_dotenv

class APICaller:
    def getURL():
        load_dotenv()
        return os.getenv('URL')

    def fetchAll():
        result = requests.get(f"{APICaller.getURL()}")
        return result

    def insertTask(name: str):
        result = requests.post(f"{APICaller.getURL()}/add", { "name": name })
        return result

    def deleteAll():
        result = requests.delete(f"{APICaller.getURL()}")
        return result


    def deleteOne(id: str):
        result = requests.delete(f"{APICaller.getURL()}/{id}")
        return result

    def update(id: str, name: str, completed: bool):
        obj = { 
            'id' : id,
            'name' : name,
            'completed' : completed
        }

        result = requests.put(f"{APICaller.getURL()}/update", obj)
        return result

    def fetchOne(id: str):
        result = requests.get(f"{APICaller.getURL()}/{id}")
        return result
