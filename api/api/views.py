from rest_framework.response import Response
from rest_framework.decorators import api_view
from taskService.taskService import TaskService

@api_view(['GET', 'DELETE'])
def tasks(request):
    if request.method == 'DELETE':
        return deleteAll()
    
    if request.method == 'GET':
        return getAll()
    
def getAll():
    service = TaskService()
    result = service.getAll()

    return Response(result)

def deleteAll():
    service = TaskService()
    return Response(service.deleteAll())

@api_view(['GET', 'DELETE'])
def onTask(request, id):
    if request.method == 'GET':
        return getOne(id)

    if request.method == 'DELETE':
        return deleteOne(id)

def getOne(id):
    try:
        service = TaskService()
        
        id = str(id)
        result = service.getOne(id)

        if result == None:
            return Response(status=404)
        
        return Response(result)    
    except:
        return Response(status=400)

def deleteOne(id):
    try:
        service = TaskService()
        
        id = str(id)
        result = service.deleteOne(id)
        if result == None:
            return Response(status=404)
        
        return Response(result, status=200)
    except:
        return Response(status=400)

@api_view(['POST'])
def addTask(request):
    try:
        service = TaskService()
        
        name = str(request.data['name'])
        result = service.addTask(name)

        return Response(result, status=201)
    except:
        return Response(status=400)

@api_view(['PUT'])
def update(request):
    try:
        service = TaskService()

        id = str(request.data['id'])
        name = str(request.data['name'])
        completed = bool(request.data['completed'])
        
        result = service.update(id, name, completed)

        if result == None:
            return Response(status=404)

        return Response(result, status=200)
    except:
        return Response(status=400)
