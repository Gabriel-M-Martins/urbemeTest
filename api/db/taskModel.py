class TaskModel:
    name: str
    completed: bool

    def __init__(self, name: str):
        self.name = name
        self.completed = False