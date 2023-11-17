from operator import attrgetter

from domain.team_member import TeamMember
from domain.user_story import UserStory
from domain.user_story_report import UserStoryReport


class Sprint:
    def __init__(self, team: [TeamMember], stores: [UserStory]):
        self.team: [TeamMember] = team
        self.stores: [UserStory] = stores
        self._members = self._members()

    def _members(self):
        while True:
            yield min(self.team, key=attrgetter('nearest_work_day'))

    def do(self) -> [UserStoryReport]:
        for story in self.stores:
            for task in story.tasks:
                member = next(self._members)
                member.do(task)

        reports = []
        for story in self.stores:
            first_task = None
            last_task = None
            for task in story.tasks:
                if first_task is None or task.start_day < first_task.start_day:
                    first_task = task
                if last_task is None or task.end_day > last_task.end_day:
                    last_task = task
            reports.append(UserStoryReport(story.id, last_task.id, first_task.start_day, last_task.end_day))
        return reports

