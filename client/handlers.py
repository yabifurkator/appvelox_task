import requests
import json
from tabulate import tabulate
from datetime import datetime

from exceptions import WrongCommandFormat
from tools import format_task, FORMATTED_TASK_COLUMNS
from config import URL


def get_all_tasks(command):
    if len(command) != 1:
        raise WrongCommandFormat(reason='количество слов в команде не равно единице.')

    url = URL + 'all/'
    response = requests.get(url=url)
    tasks_list = json.loads(response.json())
    tasks_formatted = [format_task(task) for task in tasks_list]
    
    print(response)
    print(tabulate(tasks_formatted, headers=FORMATTED_TASK_COLUMNS))
    

def create_new_task(command):
    if len(command) != 3:
        raise WrongCommandFormat(reason='количество слов в команде не равно трём.')
    
    title = command[1]
    text = command[2]

    task = {
        'title': title,
        'text': text
    }

    task_json = json.dumps(task)
    url = URL + 'new/'
    response = requests.post(url=url, json=task_json)

    print(response)


def get_task_by_id(command):
    if len(command) != 2:
        raise WrongCommandFormat(reason='количество слов в команде не равно двум.')

    data = {'pk': command[1]}
    data_json = json.dumps(data)
    url = URL + 'get/'
    response = requests.get(url=url, json=data_json)
    task_list = json.loads(response.json())
    tasks_formatted = [format_task(task) for task in task_list]

    print(response)
    print(tabulate(tasks_formatted, headers=FORMATTED_TASK_COLUMNS))


def complete_task_by_id(command):
    if len(command) != 2:
        raise WrongCommandFormat(reason='количество слов в команде не равно двум.')

    data = {'pk': command[1]}
    data_json = json.dumps(data)
    url = URL + 'complete/'
    response = requests.post(url=url, json=data_json)

    print(response)


def delete_task_by_id(command):
    if len(command) != 2:
        raise WrongCommandFormat(reason='количество слов в команде не равно двум.')

    data = {'pk': command[1]}
    data_json = json.dumps(data)
    url = URL + 'delete/'
    response = requests.post(url=url, json=data_json)

    print(response)
