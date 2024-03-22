import unittest
import json
from apicaller import APICaller

class APITester(unittest.TestCase):
    def testDeleteAll(self):
        deletionResponse = APICaller.deleteAll()
        self.assertEqual(deletionResponse.status_code, 200, "Unexpected status code.")
        
        fetchResponse = APICaller.fetchAll()
        self.assertEqual(fetchResponse.status_code, 200, "Failed to check if deletion occurred.")
        self.assertEqual(len(json.loads(fetchResponse.text)), 0, "Deletion didn't occur.")

    def testInsertTask(self):
        response = APICaller.insertTask("Do something.")
        self.assertEqual(response.status_code, 201, "Unexpected status code.")

        insertedTask = json.loads(response.text)
        insertedID = insertedTask['_id']
        expectedTask = { '_id': insertedID, 'name': 'Do something.', 'completed': False }
        self.assertDictEqual(insertedTask, expectedTask, "Inserted task is different from expected.")

        deleteOneResponse = APICaller.deleteOne(insertedID)
        self.assertEqual(deleteOneResponse.status_code, 200, "Failed to tear down insertion test.")

    def testFetchAll(self):
        deletionResponse = APICaller.deleteAll()
        self.assertEqual(deletionResponse.status_code, 200, "Failed to setup fetch all test.")

        for i in range(5):
            code = APICaller.insertTask(f"Do something {i}.").status_code
            self.assertEqual(code, 201, "Failed to setup fetch all test.")

        fetchResponse = APICaller.fetchAll()
        self.assertEqual(fetchResponse.status_code, 200, "Unexpected status code.")
        self.assertEqual(len(json.loads(fetchResponse.text)), 5, "Failed to fetch all 5 inserted tasks")

        deletionResponse = APICaller.deleteAll()
        self.assertEqual(deletionResponse.status_code, 200, "Failed to tear down fetch all test.")

    def testDeleteOne(self):
        insertResponse = APICaller.insertTask("Do something.")
        self.assertEqual(insertResponse.status_code, 201, "Failed to setup delete one test.")

        insertedTask = json.loads(insertResponse.text)
        deleteOneResponse = APICaller.deleteOne(insertedTask['_id'])
        self.assertEqual(deleteOneResponse.status_code, 200, "Failed to delete inserted task.")

        self.assertDictEqual(insertedTask, json.loads(deleteOneResponse.text))
    
    def testDeleteOne404(self):
        deleteOneResponse = APICaller.deleteOne("123456789")
        self.assertEqual(deleteOneResponse.status_code, 404, "Unexpected status code.")

    def testUpdate(self):
        insertResponse = APICaller.insertTask("Do something.")
        self.assertEqual(insertResponse.status_code, 201, "Failed to setup update test.")

        insertedTask = json.loads(insertResponse.text)
        updateResponse = APICaller.update(insertedTask['_id'], insertedTask['name'], True)

        self.assertEqual(updateResponse.status_code, 200, "Unexpected status code.")
        
        insertedTask['completed'] = True
        
        self.assertDictEqual(insertedTask, json.loads(updateResponse.text), "Failed to update inserted task.")

        deleteOneResponse = APICaller.deleteOne(insertedTask['_id'])
        self.assertEqual(deleteOneResponse.status_code, 200, "Failed to tear down update test.")

    def testFetchOne(self):
        insertResponse = APICaller.insertTask("Do something.")
        self.assertEqual(insertResponse.status_code, 201, "Failed to setup update test.")

        insertedTask = json.loads(insertResponse.text)
        fetchOneResponse = APICaller.fetchOne(insertedTask['_id'])

        self.assertEqual(fetchOneResponse.status_code, 200, "Failed to fetch inserted task.")
        self.assertDictEqual(insertedTask, json.loads(fetchOneResponse.text))

        deleteOneResponse = APICaller.deleteOne(insertedTask['_id'])
        self.assertEqual(deleteOneResponse.status_code, 200, "Failed to teardown fetch one test.")
    
    def testFetchOne404(self):
        fetchOneResponse = APICaller.fetchOne('123456789')
        self.assertEqual(fetchOneResponse.status_code, 404, "Unexpected status code.")

        
        

        


