

class UserStoryReport:
    def __init__(self, user_story_id: int, last_task_id: int, start_day: int, end_day: int):
        self.user_story_id = user_story_id
        self.last_task_id = last_task_id
        self.start_day = start_day
        self.end_day = end_day
