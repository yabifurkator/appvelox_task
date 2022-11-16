# appvelox_task

Django TODO-list REST-api

1) http://localhost:8000/all/ -> "GET" get all tasks (returns list of deserialized Task-modelds in json format)
2) http://localhost:8000/new/ -> "POST" create new task (need json in request, json format: {'title': title, 'text': text})
3) http://localhost:8000/get/ -> "GET" get task by id (need json in request, json format: {'pk': pk})
4) http://localhost:8000/complete/ -> "POST" complete task by id (need json in request, json format: {'pk': pk, 'completion_date': completion_date}, completion_date format: '%d-%m-%Y')
5) http://localhost:8000/delete/ -> "POST" delete task by id (need json in request, json format: {'pk': pk})
