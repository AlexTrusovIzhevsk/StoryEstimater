from domain.task import Task


class UserStory:
    def __init__(self, id: int, tasks: [Task]):
        self.id = id
        self.tasks = tasks
