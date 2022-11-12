import json
from datetime import datetime
from dataclasses import dataclass

from tabulate import tabulate
import requests

from exceptions import WrongCommandFormat

from tools import \
    format_task, \
    http_response_to_str, \
    FORMATTED_TASK_COLUMNS

from config import URL, HELP_MSG


@dataclass
class HandlerReturn:
    http_response: str
    handler_response: str

def get_all_tasks(command):
    if len(command) != 1:
        raise WrongCommandFormat(reason='количество слов в команде не равно единице.')

    url = URL + 'all/'
    response = requests.get(url=url)
    tasks_list = json.loads(response.json())
    tasks_formatted = [format_task(task) for task in tasks_list]

    return HandlerReturn(
        http_response=http_response_to_str(response=response),
        handler_response='\n' + tabulate(tasks_formatted, headers=FORMATTED_TASK_COLUMNS)
    ) 
    

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

    return HandlerReturn(
        http_response=http_response_to_str(response=response),
        handler_response=None
    )


def get_task_by_id(command):
    if len(command) != 2:
        raise WrongCommandFormat(reason='количество слов в команде не равно двум.')

    data = {'pk': command[1]}
    data_json = json.dumps(data)
    url = URL + 'get/'
    response = requests.get(url=url, json=data_json)
    try:
        task_list = json.loads(response.json())
    except json.decoder.JSONDecodeError:
        task_list = []
    tasks_formatted = [format_task(task) for task in task_list]

    return HandlerReturn(
        http_response=http_response_to_str(response=response),
        handler_response=('\n' + tabulate(tasks_formatted, headers=FORMATTED_TASK_COLUMNS))
            if len(tasks_formatted) != 0 else '-'
    )


def complete_task_by_id(command):
    if len(command) != 2:
        raise WrongCommandFormat(reason='количество слов в команде не равно двум.')

    data = {
        'pk': command[1],
        'completion_date': datetime.now().strftime('%d-%m-%Y')
    }
    data_json = json.dumps(data)
    url = URL + 'complete/'
    response = requests.post(url=url, json=data_json)

    return HandlerReturn(
        http_response=http_response_to_str(response=response),
        handler_response=None
    )


def delete_task_by_id(command):
    if len(command) != 2:
        raise WrongCommandFormat(reason='количество слов в команде не равно двум.')

    data = {'pk': command[1]}
    data_json = json.dumps(data)
    url = URL + 'delete/'
    response = requests.post(url=url, json=data_json)

    return HandlerReturn(
        http_response=http_response_to_str(response=response),
        handler_response=None
    )


def help_handler(command):
    if len(command) != 1:
        raise WrongCommandFormat(reason='количество слов в команде не равно единице.')

    return HandlerReturn(
        http_response=None,
        handler_response=HELP_MSG
    )    
