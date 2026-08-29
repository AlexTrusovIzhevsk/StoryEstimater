from domain.task import Task


class TeamMember:
    def __init__(self, id: int, story_point_per_day: float, max_day: int):
        self.id = id
        self.nearest_work_day = 0
        self.max_day = max_day
        self.story_point_per_day = story_point_per_day
        self.remains_sp = story_point_per_day

    def is_ended_sprint(self) -> bool:
        return self.nearest_work_day >= self.max_day

    def do(self, task: Task) -> bool:
        current_nearest_work_day = self.nearest_work_day
        if self.max_day > self.nearest_work_day:
            self._do(task)
            return current_nearest_work_day is not self.nearest_work_day
        return False

    def _end_task(self, task: Task, start_day) -> None:
        task.current_story_point = 0
        task.start_day = start_day
        task.end_day = self.nearest_work_day

    def _do(self, task: Task) -> None:
        start_day = self.nearest_work_day
        if self.remains_sp == task.current_story_point:
            self.remains_sp = self.story_point_per_day
            self._end_task(task, start_day)
            self.nearest_work_day += 1
        elif self.remains_sp > task.current_story_point:
            self.remains_sp -= task.current_story_point
            self._end_task(task, start_day)
        else:
            task.current_story_point -= self.remains_sp
            self.nearest_work_day += 1
            self.remains_sp = self.story_point_per_day

            day_count = task.current_story_point // self.story_point_per_day
            if day_count > 0:
                # что если nearest_work_day + day_count > длинны спринта?
                # В текущей реализации разраб уходит с ней в следующий српинт
                last_day_remains_sp = task.current_story_point % self.story_point_per_day
                task.current_story_point = last_day_remains_sp
                self.nearest_work_day += day_count - 1
                if last_day_remains_sp == 0:
                    self._end_task(task, start_day)
                    self.nearest_work_day += 1
                else:
                    self._end_task(task, start_day)
            else:
                self._end_task(task, start_day)
