
class Task:
    def __init__(self, id: int, story_point: int):
        self.id = id
        self.story_point = story_point
        self.current_story_point = story_point
        self.start_day = -1
        self.end_day = -1