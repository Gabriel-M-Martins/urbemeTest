from db.dbhandler import DBHandler
from db.taskModel import TaskModel

class TaskService:
    def __init__(self):
        self.db = DBHandler()

    def __clearUpResult(task: TaskModel | None):
        if task != None:
            task['_id'] = str(task['_id'])
        
        return task

    def getAll(self):
        result = []
        for task in self.db.getAll():
            task = TaskService.__clearUpResult(task)
            result.append(task)
        
        return result
    
    def getOne(self, id: str):
        return TaskService.__clearUpResult(self.db.getOne(id))
    
    def addTask(self, name: str):
        result = self.db.insert(TaskModel(name))

        return TaskService.__clearUpResult(result)
    
    def deleteOne(self, id: str):
        result = self.db.delete(id)
        return TaskService.__clearUpResult(result)
    
    def deleteAll(self):
        result = self.db.deleteAll()
        return { 'deleted' : result }
    
    def update(self, id: str, name: str, completed: bool):
        task = TaskModel(name)
        task.completed = completed

        result = self.db.update(id, task)
        return TaskService.__clearUpResult(result)

