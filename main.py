import json

from domain.sprint import Sprint
from domain.task import Task
from domain.team_member import TeamMember
from domain.user_story import UserStory
from domain.user_story_report import UserStoryReport


def _print_report(reports: [UserStoryReport]):
    for report in reports:
        print(f'us_id:{report.user_story_id}, last_task_id:{report.last_task_id}, start_day:{report.start_day}, end_day:{report.end_day}')


def main_console():
    sprint_day_count = int(input())
    team = [TeamMember(i, int(s), sprint_day_count + 1) for (i, s) in enumerate(input().split())]
    stories_count = int(input())
    stories = []
    for us_id in range(stories_count):
        tasks = [Task(i, int(s)) for (i, s) in enumerate(input().split())]
        stories.append(UserStory(us_id, tasks))

    sprint = Sprint(team, stories)

    reports = sprint.do()

    _print_report(reports)



def main_json():
    text ="""
    {
      "sprint_day_count": 10,
      "story_point_per_day": [
        4,
        5.3,
        6.3,
        6.3,
        5.3,
        6.3,
        6.3,
        6.3
      ],
      "stories_count": 9,
      "stories": [
        {"291519": [5]},
        {"302497": [2]},
        {"261848": [3, 6, 2]},
        {"281930": [1, 2, 3, 4]},
        {"302741": [2]},
        {"300066": [4, 4, 7]},
        {"293426": [9, 16, 9, 6, 8]},
        {"300594": [6, 7]},
        {"293390": [7]}
      ]
    }"""
    data = json.loads(text)
    sprint_day_count = data['sprint_day_count']
    story_point_per_day = data['story_point_per_day']
    stories_data = data['stories']


    team = [TeamMember(i, s * 0.4, sprint_day_count + 1) for (i, s) in enumerate(story_point_per_day)]
    stories = []
    for stories_data in stories_data:
        key = next(enumerate(stories_data.keys()))[1]
        us_id = int(key)
        task_data = stories_data[key]
        tasks = [Task(i, int(s)) for (i, s) in enumerate(task_data)]
        stories.append(UserStory(int(us_id), tasks))

    sprint = Sprint(team, stories)
    reports = sprint.do()
    _print_report(reports)



# main_console()
main_json()
