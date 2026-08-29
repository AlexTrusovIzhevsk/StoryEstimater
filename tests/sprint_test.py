from unittest import TestCase

from domain.sprint import Sprint
from domain.task import Task
from domain.team_member import TeamMember
from domain.user_story import UserStory


class SprintTest(TestCase):

    def test_one_day(self):
        sprint_day_count = 1
        story_point_per_day = 1
        team = [TeamMember(1, story_point_per_day, sprint_day_count)]
        story_point_task = 1
        tasks = [Task(1, story_point_task)]
        stores = [UserStory(1, tasks)]
        sprint = Sprint(team, stores)

        reports = sprint.do()

        self.assertEqual(1, len(reports))
        report = reports.pop()
        self.assertEqual(0, report.start_day)
        self.assertEqual(0, report.end_day)

    def test_many_day(self):
        sprint_day_count = 3
        story_point_per_day = 1
        team = [TeamMember(1, story_point_per_day, sprint_day_count)]
        story_point_task = 3
        tasks = [Task(1, story_point_task)]
        stores = [UserStory(1, tasks)]
        sprint = Sprint(team, stores)

        reports = sprint.do()

        self.assertEqual(1, len(reports))
        report = reports.pop()
        self.assertEqual(0, report.start_day)
        self.assertEqual(2, report.end_day)

    def test_many_task(self):
        sprint_day_count = 3
        story_point_per_day = 1
        team = [TeamMember(1, story_point_per_day, sprint_day_count)]
        story_point_task = 1
        tasks = [Task(1, story_point_task), Task(1, story_point_task), Task(1, story_point_task)]
        stores = [UserStory(1, tasks)]
        sprint = Sprint(team, stores)

        reports = sprint.do()

        self.assertEqual(1, len(reports))
        report = reports.pop()
        self.assertEqual(0, report.start_day)
        self.assertEqual(2, report.end_day)

    def test_many_us(self):
        sprint_day_count = 3
        story_point_per_day = 1
        team = [TeamMember(1, story_point_per_day, sprint_day_count)]
        story_point_task = 1
        tasks1 = [Task(1, story_point_task)]
        tasks2 = [Task(2, story_point_task)]
        tasks3 = [Task(3, story_point_task)]
        stores = [UserStory(1, tasks1), UserStory(2, tasks2), UserStory(3, tasks3)]
        sprint = Sprint(team, stores)

        reports = sprint.do()

        self.assertEqual(3, len(reports))
        report3 = reports.pop()
        report2 = reports.pop()
        report1 = reports.pop()
        self.assertEqual(0, report1.start_day)
        self.assertEqual(0, report1.end_day)
        self.assertEqual(1, report2.start_day)
        self.assertEqual(1, report2.end_day)
        self.assertEqual(2, report3.start_day)
        self.assertEqual(2, report3.end_day)

    def test_task_more_one_day(self):
        sprint_day_count = 6
        story_point_per_day = 1
        team = [TeamMember(1, story_point_per_day, sprint_day_count)]
        story_point_task = 3
        tasks1 = [Task(1, story_point_task)]
        tasks2 = [Task(2, story_point_task)]
        stores = [UserStory(1, tasks1), UserStory(2, tasks2)]
        sprint = Sprint(team, stores)

        reports = sprint.do()

        self.assertEqual(2, len(reports))
        report2 = reports.pop()
        report1 = reports.pop()
        self.assertEqual(0, report1.start_day)
        self.assertEqual(2, report1.end_day)
        self.assertEqual(3, report2.start_day)
        self.assertEqual(5, report2.end_day)

    def test_many_task_in_day(self):
        sprint_day_count = 2
        story_point_per_day = 3
        team = [TeamMember(1, story_point_per_day, sprint_day_count)]
        story_point_task = 2
        tasks1 = [Task(1, story_point_task)]
        tasks2 = [Task(2, story_point_task)]
        tasks3 = [Task(3, story_point_task)]
        stores = [UserStory(1, tasks1), UserStory(2, tasks2), UserStory(3, tasks3)]
        sprint = Sprint(team, stores)

        reports = sprint.do()

        self.assertEqual(3, len(reports))
        report3 = reports.pop()
        report2 = reports.pop()
        report1 = reports.pop()
        self.assertEqual(0, report1.start_day)
        self.assertEqual(0, report1.end_day)
        self.assertEqual(0, report2.start_day)
        self.assertEqual(1, report2.end_day)
        self.assertEqual(1, report3.start_day)
        self.assertEqual(1, report3.end_day)


    def test_two_men(self):
        sprint_day_count = 3
        story_point_per_day = 1
        men1 = TeamMember(1, story_point_per_day, sprint_day_count)
        men2 = TeamMember(2, story_point_per_day, sprint_day_count)
        team = [men1, men2]
        tasks1 = [Task(1, 3)]
        tasks2 = [Task(2, 1), Task(3, 2)]
        stores = [UserStory(1, tasks1), UserStory(2, tasks2)]
        sprint = Sprint(team, stores)

        reports = sprint.do()

        self.assertEqual(2, len(reports))
        report2 = reports.pop()
        report1 = reports.pop()
        self.assertEqual(0, report1.start_day)
        self.assertEqual(2, report1.end_day)
        self.assertEqual(0, report2.start_day)
        self.assertEqual(2, report2.end_day)


    def test_team(self):
        sprint_day_count = 4
        story_point_per_day = 1
        men1 = TeamMember(1, story_point_per_day, sprint_day_count)
        men2 = TeamMember(2, story_point_per_day, sprint_day_count)
        men3 = TeamMember(3, story_point_per_day, sprint_day_count)
        team = [men1, men2, men3]
        tasks1 = [Task(1, 3)]
        tasks2 = [Task(2, 2)]
        tasks3 = [Task(3, 1), Task(4, 2), Task(5, 1)]
        stores = [UserStory(1, tasks1), UserStory(2, tasks2), UserStory(2, tasks3)]
        sprint = Sprint(team, stores)

        reports = sprint.do()

        self.assertEqual(3, len(reports))
        report3 = reports.pop()
        report2 = reports.pop()
        report1 = reports.pop()
        self.assertEqual(0, report1.start_day)
        self.assertEqual(2, report1.end_day)
        self.assertEqual(0, report2.start_day)
        self.assertEqual(1, report2.end_day)
        self.assertEqual(0, report3.start_day)
        self.assertEqual(2, report3.end_day)

