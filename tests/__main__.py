import requests
import json
import os
from dotenv import load_dotenv


class AutoTester:
    def run():
        if AutoTester.deleteAll():
            allTasks = AutoTester.fetchAll()
            if type(allTasks) == str:
                print("Delete All: Failed.")
            else:
                if len(allTasks) > 0:
                    print("Delete All: Failed.")
                else:
                    print("Delete All: Succeeded.")
        else:
            print("Delete All: Failed.")

        task = AutoTester.insertTask("Do something.")
        if task == "Error":
            print("Insert Task: Failed.")
        else:
            if '"name":"Do something."' not in task and '"completed":false' not in task:
                print("Insert Task: Failed.")
            else:
                print("Insert Task: Succeeded.")
        
        allTasks = AutoTester.fetchAll()
        if type(allTasks) == str:
            print("Fetch All: Failed.")
        else:
            if len(allTasks) == 1:
                print("Fetch All: Succeeded.")
            else:
                print("Fetch All: Failed.")

        AutoTester.deleteAll()
        task = AutoTester.insertTask("Do something.")
        if task == "Error":
            print("Update Task: Failed.")
        else:
            task = json.loads(task)
            id = task['_id']
            updatedTask = AutoTester.update(id, "Do something.", True)
            if updatedTask == "Error":
                print("Update Task: Failed.")
            else:
                if f'"id":"{id}"' not in updatedTask and '"name":"Do something."' not in updatedTask and '"completed":true' not in updatedTask:
                    print("Update Task: Failed.")
                else:
                    print("Update Task: Succeeded.")

        AutoTester.deleteAll()
        task = AutoTester.insertTask("Do something.")
        if task == "Error":
            print("Delete Task: Failed.")
        else:
            task = json.loads(task)
            id = task['_id']
            deletedTask = AutoTester.deleteOne(id)
            if deletedTask == "Error":
                print("Delete Task: Failed.")
            else:
                print("Delete Task: Succeeded.")

        AutoTester.deleteAll()
        task = AutoTester.insertTask("Do something.")
        if task == "Error":
            print("Fetch Task: Failed.")
        else:
            task = json.loads(task)
            id = task['_id']
            name = task['name']
            completed = task['completed']

            fetchedTask = AutoTester.fetchOne(id)
            if fetchedTask == "Error":
                print("Fetch Task: Failed.")
            else:
                fetchedTask = json.loads(fetchedTask)
                fetchedId = fetchedTask['_id']
                fetchedName = fetchedTask['name']
                fetchedCompleted = fetchedTask['completed']

                if id != fetchedId or name != fetchedName or completed != fetchedCompleted:
                    print("Fetch Task: Failed.")
                else:
                    print("Fetch Task: Succeeded.")

        AutoTester.deleteAll()
        

    def getURL():
        load_dotenv()
        return os.getenv('URL')

    def fetchAll():
        result = requests.get(f"{AutoTester.getURL()}")
        if not result.ok:
            return "Error"
        
        return json.loads(result.text)

    def insertTask(name: str):
        result = requests.post(f"{AutoTester.getURL()}/add", { "name": name })
        if not result.ok:
            return "Error"
        
        return result.text

    def deleteAll():
        result = requests.delete(f"{AutoTester.getURL()}")
        return result.ok


    def deleteOne(id: str):
        result = requests.delete(f"{AutoTester.getURL()}/{id}")
        if not result.ok:
            return "Error"
        
        return result.text

    def update(id: str, name: str, completed: bool):
        obj = { 
            'id' : id,
            'name' : name,
            'completed' : completed
        }

        result = requests.put(f"{AutoTester.getURL()}/update", obj)
        
        if not result.ok:
            return "Error"
        
        return result.text

    def fetchOne(id: str):
        result = requests.get(f"{AutoTester.getURL()}/{id}")
        
        if not result.ok:
            return "Error"
        
        return result.text


AutoTester.run()