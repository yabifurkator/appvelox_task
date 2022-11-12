FORMATTED_TASK_COLUMNS = ['ID', 'Title', 'Text', 'Completion Date', 'Completed']

def format_task(task):
    task_fields = task['fields']

    pk = task['pk']
    title = task_fields['title']
    text = task_fields['text']
    completion_date = task_fields['completion_date']
    completed = task_fields['completed']

    if completion_date is None:
        completion_date = '-'
    if completed:
        completed = '✔'
    else:
        completed = '✘'

    return [pk, title, text, completion_date, completed]


def http_response_to_str(response):
    return str(response) + ' -> ' + response.headers['message']
