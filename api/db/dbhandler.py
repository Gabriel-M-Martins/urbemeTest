from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId
from db.taskModel import TaskModel
import os
from dotenv import load_dotenv

class DBHandler:
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(os.getenv('MONGO_CONNECTION'))
        self.db = self.client.todo
        self.tasks = self.db.tasks

    def insert(self, task: TaskModel):
        result = self.tasks.insert_one(vars(task))
        return self.tasks.find_one({ "_id" : result.inserted_id })
    
    def delete(self, id: str):
        try:
            return self.tasks.find_one_and_delete({ "_id" : ObjectId(id) })
        except:
            return None
        
    def deleteAll(self):
        result = self.tasks.delete_many({})
        return result.deleted_count

    def update(self, old_id: str, new: TaskModel):
        try:
            self.tasks.update_one({ "_id" : ObjectId(old_id) }, { "$set": { "name": new.name, "completed": new.completed } })
            return self.tasks.find_one({ "_id" : ObjectId(old_id) })
        except:
            return None
    
    def getAll(self):
        cursor = self.tasks.find({})
        return list(cursor)
    
    def getOne(self, id: str):
        try:
            return self.tasks.find_one({ "_id" : ObjectId(id) })
        except:
            return None

